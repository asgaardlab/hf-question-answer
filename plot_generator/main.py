from data_cleaner.discussion_reader import get_all_questions, get_all_discussions, save_all_discussions, \
    save_all_questions
from plot_generator.discussion_participants_calculator import calculate_discussions_participants
from plot_generator.discussion_participants_visualizer import visualize_discussion_participants, \
    compare_response_by_team_participation
from plot_generator.discussion_response_analyzer import calculate_discussions_responses, calculate_response_length, \
    calculate_has_owner_responses, calculate_discussions_contributors_responses
from plot_generator.discussion_response_visualizer import visualize_discussion_response, compare_response_by_status, \
    visualize_response_length, compare_response_length_per_status
from plot_generator.discussion_status_analyzer import get_discussions_status
from plot_generator.discussion_status_visualizer import visualize_discussion_status_by_team_participation
from plot_generator.discussion_time_range_calculator import calculate_discussions_creation_time, \
    calculate_discussions_response_delay
from plot_generator.discussion_time_range_visualizer import visualize_discussion_response_delays, \
    visualize_discussion_creation_time_range
from util import path

if __name__ == '__main__':
    print('Generating plots...')

    path.PLOTS_DIRECTORY.mkdir(parents=True, exist_ok=True)

    all_discussions = get_all_discussions()
    calculate_discussions_creation_time(all_discussions)
    visualize_discussion_creation_time_range(all_discussions)
    save_all_discussions(all_discussions)

    all_questions = get_all_questions()

    all_questions = calculate_discussions_responses(all_questions)
    visualize_discussion_response(all_questions)

    all_questions = get_discussions_status(all_questions)
    compare_response_by_status(all_questions)

    all_questions = calculate_response_length(all_questions)
    visualize_response_length(all_questions)

    compare_response_length_per_status(all_questions)

    all_questions = calculate_discussions_participants(all_questions)
    visualize_discussion_participants(all_questions)

    all_questions = calculate_has_owner_responses(all_questions)
    all_questions = calculate_discussions_contributors_responses(all_questions)
    compare_response_by_team_participation(all_questions)

    visualize_discussion_status_by_team_participation(all_questions)

    all_questions = calculate_discussions_creation_time(all_questions)
    all_questions = calculate_discussions_response_delay(all_questions)
    visualize_discussion_response_delays(all_questions)

    save_all_questions(all_questions)
