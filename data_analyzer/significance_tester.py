from scipy.stats import mannwhitneyu

from data_cleaner.discussion_reader import get_all_questions
from cliffs_delta import cliffs_delta


def significance_test(data1: list[int], data2: list[int]) -> tuple[float, float]:
    stat, p = mannwhitneyu(data1, data2)
    print(stat, p)

    alpha = 0.05
    if p > alpha:
        print('Same distribution')
    else:
        print('Different distribution')

    return stat, p


def calculate_effect_size(data1: list[int], data2: list[int]):
    delta, size = cliffs_delta(data1, data2)

    print(f"Cliff's delta: {delta}")
    print(f"Effect size interpretation: {size}")


def response_participants_significance_test(discussions):
    response_with_team_participation = \
        discussions[(discussions['has_owner_responses'] == True) | (discussions['no_of_contributor_responses'] > 0)][
            'no_of_responses'].values.tolist()
    print(','.join(map(str, response_with_team_participation)))

    response_without_team_participation = \
        discussions[(discussions['has_owner_responses'] == False) & (discussions['no_of_contributor_responses'] == 0)][
            'no_of_responses'].values.tolist()
    print(','.join(map(str, response_without_team_participation)))

    print('Response based on team participation')
    stat, p = significance_test(response_with_team_participation, response_without_team_participation)
    calculate_effect_size(response_with_team_participation, response_without_team_participation)


def response_status_significance_test(discussions):
    open_responses = discussions[discussions['status'] == 'open']['no_of_responses'].values.tolist()
    print(','.join(map(str, open_responses)))

    closed_responses = discussions[discussions['status'] == 'closed']['no_of_responses'].values.tolist()
    print(','.join(map(str, closed_responses)))

    print('Response based on status')
    significance_test(open_responses, closed_responses)
    calculate_effect_size(open_responses, closed_responses)


def sample_test():
    males = [19, 22, 16, 29, 24, 62, 45, 90, 76, 45]
    print(males)

    females = [20, 11, 17, 12, 21, 15, 19, 23, 16, 18]
    print(females)

    significance_test(males, females)


def length_status_significance_test(discussions):
    open_discussions = discussions[discussions['status'] == 'open']['length'].values.tolist()
    closed_discussions = discussions[discussions['status'] == 'closed']['length'].values.tolist()

    print('Length based on status')
    significance_test(open_discussions, closed_discussions)
    calculate_effect_size(open_discussions, closed_discussions)


if __name__ == '__main__':
    # sample_test()

    questions = get_all_questions()
    length_status_significance_test(questions)
    response_status_significance_test(questions)
    response_participants_significance_test(questions)
