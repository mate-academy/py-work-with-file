import csv


def create_report(data_file_name: str, report_file_name: str) -> str:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):

        reader = csv.reader(data_file)
        report = {"supply": 0, "buy": 0}

        for row in reader:
            key, value = row
            report[key] += int(value)

        for key, value in report.items():
            report_file.write(f"{key},{value}\n")

        report_file.write(f"result,{report['supply'] - report['buy']}\n")
