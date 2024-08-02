from data_analyzer.discussion_length_calculator import calculate_random_discussion_lengths
from data_cleaner.discussion_reader import get_all_random_discussions, save_selected_random_discussions
from data_cleaner.hidden_body_identifier import save_random_hidden_discussions
from data_cleaner.main import filter_discussions
from data_cleaner.main_statistics_provider import provide_discussion_filtering_statistics
from data_cleaner.non_english_identifier import save_random_non_english_discussions

if __name__ == '__main__':
    # save_random_hidden_discussions()
    # calculate_random_discussion_lengths()
    # save_random_non_english_discussions()

    all_random_discussions = get_all_random_discussions()
    cleaned_random_discussions = filter_discussions(all_random_discussions)
    save_selected_random_discussions(cleaned_random_discussions)

    provide_discussion_filtering_statistics(all_random_discussions)
    