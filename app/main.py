import csv


def create_report(data_file_name: str, report_file_name: str):
    totals = {'supply': 0, 'buy': 0}

    with open(data_file_name, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row:
                continue
            operation, amount = row[0], row[1]
            totals[operation] += int(amount)

    result = totals['supply'] - totals['buy']

    with open(report_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['supply', totals['supply']])
        writer.writerow(['buy', totals['buy']])
        writer.writerow(['result', result])

