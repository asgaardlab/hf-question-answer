from datetime import datetime
from pathlib import Path

import yaml

from data_collector.type.CustomLoader import CustomLoader
from util import path


class Discussion:
    def __init__(self, discussion_number: int, model_id: str, discussion_status: str, author: str, created_at: datetime,
                 heading: str, description: str, is_hidden: bool = False, full_raw_discussion: str = None,
                 status: str = None):
        self.discussion_number = discussion_number
        self.model_id = model_id
        self.heading = heading
        self.description = description
        self.discussion_status = discussion_status
        self.author = author
        self.created_at = created_at
        self.url = f'https://huggingface.co/{model_id}/discussions/{discussion_number}'
        self.is_hidden = is_hidden
        self.full_raw_discussion = full_raw_discussion
        self.discussion_status = status

    @staticmethod
    def from_path_str(file_path: str):
        return Discussion.from_path(path.DISCUSSIONS_DIRECTORY / file_path)

    @staticmethod
    def from_path(file_path: Path):
        if file_path.name.startswith('error'):
            return None

        raw_discussion = yaml.load(file_path.open('r'), Loader=CustomLoader)
        first_comment = raw_discussion['events'][0]
        return Discussion(raw_discussion['num'], raw_discussion['repo_id'], raw_discussion['status'],
                          first_comment['author'], first_comment['created_at'], raw_discussion['title'],
                          first_comment['content'], first_comment['hidden'], raw_discussion, raw_discussion['status'])

    def get_model_dir_name(self):
        dir_name = self.model_id.replace('/', '@')
        if dir_name[-1] == ".":
            dir_name = dir_name[:-1] + "$"
        return dir_name

    def get_post(self) -> str:
        return self.heading + '\n\n' + self.description

    def get_responses(self) -> list[str]:
        responses = []
        discussion_events = self.full_raw_discussion['events']
        for event in discussion_events:
            if event['type'] == 'comment':
                responses.append(event['content'])
        responses.pop(0)
        return responses

    def get_participants(self) -> set[str]:
        participants = set()
        discussion_events = self.full_raw_discussion['events']
        for event in discussion_events:
            if event['type'] == 'comment':
                participants.add(event['author'])
        return participants

    def get_contributor_responses(self) -> list[str]:
        contributor_responses = []
        discussion_events = self.full_raw_discussion['events']
        for event in discussion_events:
            if event['type'] == 'comment':
                if 'author' in event['_event'] and event['_event']['author']['isOrgMember']:
                    # print(self.url, event['_event']['author']['name'])
                    contributor_responses.append(event['content'])
        # return len([event for event in discussion_events if event['type'] == 'comment' and not event['hidden']])
        return contributor_responses

    def get_first_response_delay(self) -> datetime | None:
        discussion_events = self.full_raw_discussion['events']
        comments = [event for event in discussion_events if event['type'] == 'comment']
        if len(comments) > 1:
            return comments[1]['created_at'] - self.created_at
        return None

    def get_status(self) -> str:
        return self.discussion_status

    def get_status_changes_count(self) -> int:
        discussion_events = self.full_raw_discussion['events']
        return len([event for event in discussion_events if event['type'] == 'status-change'])

    def get_identified_language(self) -> str:
        discussion_events = self.full_raw_discussion['events']
        for event in discussion_events:
            if event['type'] == 'comment':
                if 'identifiedLanguage' in event['_event']['data'].keys():
                    return event['_event']['data']['identifiedLanguage']['language']
                return 'en'

    def has_owner_response(self) -> bool:
        discussion_events = self.full_raw_discussion['events']
        for event in discussion_events:
            if event['type'] == 'comment' and 'author' in event['_event'].keys() and event['_event']['author'][
                'isOwner']:
                return True
        return False

    def get_full_discussion(self) -> str:
        full_discussion = self.full_raw_discussion['title']
        discussion_events = self.full_raw_discussion['events']
        for event in discussion_events:
            if event['type'] == 'comment' and not event['hidden']:
                full_discussion += f'\n\n{event["content"]}'
        return full_discussion

    def get_discussion_closer_status(self) -> str:
        if self.discussion_status == 'open':
            return 'open'

        discussion_events = self.full_raw_discussion['events']
        discussion_status_change_events = [event for event in discussion_events if event['type'] == 'status-change']

        if not discussion_status_change_events:
            return 'open'

        closing_event = discussion_status_change_events[-1]

        if closing_event['author'] == self.author:
            return 'self'
        closer = closing_event['_event']['author']
        if closer['isOwner']:
            return 'owner'
        if closer['isOrgMember']:
            return 'contributor'

        return 'other'
