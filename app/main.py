import csv


def create_report(data_file_name: str, report_file_name: str):
    total_supply = 0
    total_buy = 0

    with open(data_file_name, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if len(row) == 2:
                operation_type = row[0].strip()
                try:
                    amount = int(row[1].strip())
                except ValueError:
                    continue

                if operation_type == 'supply':
                    total_supply += amount
                elif operation_type == 'buy':
                    total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['supply', total_supply])
        writer.writerow(['buy', total_buy])
        writer.writerow(['result', result])
