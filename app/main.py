import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with (
        open(data_file_name, "r") as csvfile,
        open(report_file_name, "w") as report_file
    ):
        csv_reader = csv.reader(csvfile, delimiter=",")
        for row in csv_reader:
            if row[0] == "supply":
                supply += int(row[1])
            if row[0] == "buy":
                buy += int(row[1])
        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
