import gspread
from sklearn.metrics import cohen_kappa_score


def calculate_irr(start_row, end_row):
    gc = gspread.oauth()
    workbook = gc.open_by_key('16He8cXBM0SXIdqqWMqLXqQru3ICst30YSNl5V365iak')

    column = 'C'

    cell_range = f'{column}{start_row}:{column}{end_row}'

    author1_labels_worksheet = workbook.worksheet('author1_labels')
    author1_submappings = author1_labels_worksheet.get(cell_range)
    author1_submappings = [item[0] for item in author1_submappings if item]
    print(len(author1_submappings), author1_submappings)

    author2_labels_worksheet = workbook.worksheet('author2_labels')
    author2_submappings = author2_labels_worksheet.get(cell_range)
    author2_submappings = [item[0] for item in author2_submappings if item]
    print(len(author2_submappings), author2_submappings)

    kappa = cohen_kappa_score(author1_submappings, author2_submappings)
    print(f'Kappa: {kappa}')


if __name__ == '__main__':
    calculate_irr(12, 62)
    calculate_irr(12, 62)
