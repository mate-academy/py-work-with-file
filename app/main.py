import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    result = {}
    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            result[row[0]] = row[1]

    with open(report_file_name, "w", newline='') as file2:
        writer = csv.writer(file2)
        for name, value in result.items():
            writer.writerow([name, value])
