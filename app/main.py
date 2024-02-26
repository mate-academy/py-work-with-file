import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {}

    with open(data_file_name, "r") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            key, value = row
            data[key] += value
        for line in data_file.readlines():
            data[line.split(",")[0]] += line.split(",")[1]

    with open(report_file_name, "w", newline='') as report_file:
        writer = csv.writer(report_file)
        for key, value in data.items():
            writer.writerow([key, value])
