import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as csvfile,
        open(report_file_name, "w") as outfile
    ):
        reader = csv.reader(csvfile)
        report = {"supply": 0, "buy": 0}

        for row in reader:
            key, value = row
            report[key] += int(value)

        for key, value in report.items():
            outfile.write(f"{key},{value}\n")

        outfile.write(f"result,{report['supply'] - report['buy']}\n")
