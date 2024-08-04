import pandas as pd
from sklearn.metrics import cohen_kappa_score

from util import path


def calculate_irr(start_row, end_row):
    manual_question_mappings = pd.read_excel(path.DATA_DIRECTORY / 'manual_question_mapping.xlsx', sheet_name=['author1_labels', 'author2_labels'], na_filter=False)

    author1_mappings = manual_question_mappings['author1_labels']['mapping'].iloc[start_row:(end_row+1)].values
    author1_non_empty_mappings = [mapping for mapping in author1_mappings if mapping != '']

    author2_mappings = manual_question_mappings['author2_labels']['mapping'].iloc[start_row:(end_row+1)].values
    author2_non_empty_mappings = [mapping for mapping in author2_mappings if mapping != '']

    print(len(author1_non_empty_mappings), len(author2_non_empty_mappings))

    kappa = cohen_kappa_score(author1_non_empty_mappings, author2_non_empty_mappings)
    print(f'Kappa: {kappa}')


if __name__ == '__main__':
    calculate_irr(165, 265)
    calculate_irr(266, 431)
