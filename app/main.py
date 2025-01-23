import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    operations ={}
    for row in data:
        operation_type  = row[0]
        amount = int(row[1])
        if operation_type in operations:
            operations[operation_type] += amount
        else:
            operations[operation_type] = amount

    with open(report_file_name, "w", newline="") as report_file:
        csv_writer = csv.writer(report_file)
        for operations, total_amount in operations.items():
            csv_writer.writerow([operations, total_amount])
