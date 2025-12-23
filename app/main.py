import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):
        reader = csv.reader(file_in)
        report = {"supply": 0, "buy": 0}

        for row in reader:
            key, value = row
            report[key] += int(value)

        for key, value in report.items():
            file_out.write(f"{key},{value}\n")

        file_out.write(f"result,{report['supply'] - report['buy']}\n")
