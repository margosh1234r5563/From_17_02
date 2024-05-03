def days_in_month(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 28


def calculate_days(date, current_date):
    day1, month1 = map(int, date.split('.'))
    day2, month2 = current_date
    if month2 < month1:
        month2 = month2 + 12
    return (month2 - month1) * 31 + day2 - day1


def check_storage(input_file, output_file):
    with open(input_file, 'r') as f:
        current_date = list(map(int, f.readline().strip().split('.')))
        n = int(f.readline().strip())
        storage = []
        for _ in range(n):
            cell, date = f.readline().strip().split()
            storage.append((int(cell), date))

    result = [cell for cell, date in storage if calculate_days(date, current_date) > 3]

    with open(output_file, 'w') as f:
        for cell in result:
            f.write(str(cell) + '\n')


check_storage('input_10', 'output_10')
