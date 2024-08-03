from data_cleaner.discussion_reader import get_all_questions, get_all_discussions
from plot_generator.discussion_participants_visualizer import visualize_discussion_participants, \
    compare_response_by_team_participation
from plot_generator.discussion_response_visualizer import visualize_discussion_response, compare_response_by_status, \
    visualize_response_length, compare_response_length_per_status
from plot_generator.discussion_status_visualizer import visualize_discussion_status_by_team_participation
from plot_generator.discussion_time_range_visualizer import visualize_discussion_response_delays, \
    visualize_discussion_creation_time_range

if __name__ == '__main__':
    all_discussions = get_all_discussions()
    visualize_discussion_creation_time_range(all_discussions)

    all_questions = get_all_questions()

    visualize_discussion_response(all_questions)
    compare_response_by_status(all_questions)

    visualize_response_length(all_questions)
    compare_response_length_per_status(all_questions)

    visualize_discussion_participants(all_questions)
    compare_response_by_team_participation(all_questions)

    visualize_discussion_status_by_team_participation(all_questions)

    visualize_discussion_response_delays(all_questions)
