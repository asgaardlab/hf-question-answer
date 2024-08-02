from pathlib import Path

import openai
from openai import OpenAI, RateLimitError, BadRequestError

from data_collector.type.discussion import Discussion
from util import path, helper, constants


def request_to_gpt(client: OpenAI, discussion: Discussion) -> openai.resources.chat.completions.Completions:
    with open(path.SYSTEM_PROMPT_FILE, 'r') as f:
        instruction_content = f.read()

    request_content = discussion.get_post()

    return client.chat.completions.create(
        model='gpt-3.5-turbo-0125',
        messages=[{
            'role': 'system',
            'content': instruction_content
        }, {
            'role': 'user',
            'content': request_content
        }]
    )


def save_response(discussion: Discussion, discussion_id: int, response: openai.resources.chat.completions.Completions) -> None:
    print(discussion_id)
    print(response.choices[0].message.content)
    gpt35_result_file_path = get_save_file_name(discussion, discussion_id)
    with open(gpt35_result_file_path, 'w', encoding='utf-8') as f:
        f.write(f'## {discussion.url}\n\n')
        f.write(response.choices[0].message.content)


def get_save_file_name(save_directory: Path, discussion: Discussion, discussion_id: int) -> Path:
    file_name_prefix = f'{discussion_id}_{helper.get_model_dir_name(discussion.model_id)}_{discussion.discussion_number}'
    gpt35_result_file_path = save_directory / f'{file_name_prefix}_result_gpt-3-5.md'
    return gpt35_result_file_path


def classify_discussion(client: OpenAI, discussion_path: str, discussion_id: int, save_directory: Path) -> None:
    discussion = Discussion.from_path_str(discussion_path)
    if not get_save_file_name(save_directory, discussion, discussion_id).exists():
        try:
            response = request_to_gpt(client, discussion)
            save_response(discussion, discussion_id, response)
        except RateLimitError as rle:
            print(rle)
        except BadRequestError as bre:
            print(bre)
        except FileNotFoundError as fnfe:
            print(fnfe)
    else:
        print(f'{discussion_id} already exists')


def classify_discussions(discussions, save_directory: Path) -> None:
    client = OpenAI(
        api_key=constants.OPENAI_API_KEY
    )

    print(f'Classifying {len(discussions)} discussions')
    discussions.apply(
        lambda discussion: classify_discussion(client, discussion.discussion_path, discussion['index'], save_directory), axis=1)
