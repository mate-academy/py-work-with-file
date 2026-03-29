import csv


def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) != 2:
                continue

            operation, amount = row

            try:
                amount = int(amount)
            except ValueError:
                continue

            if operation == 'supply':
                supply += amount
            elif operation == 'buy':
                buy += amount

    result = supply - buy

    with (
        open(report_file_name,
             mode='w',
             encoding='utf-8',
             newline='')
        as file
    ):
        writer = csv.writer(file)
        writer.writerow(['supply', supply])
        writer.writerow(['buy', buy])
        writer.writerow(['result', result])
