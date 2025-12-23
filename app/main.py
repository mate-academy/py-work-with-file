import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as input_file,
        open(report_file_name, "w", newline="") as out_file
    ):
        input_file_csv = csv.reader(input_file, delimiter=",")

        supply = 0
        buy = 0
        for name, value in input_file_csv:
            if name == "supply":
                supply += int(value)
            else:
                buy += int(value)
        report = [
            ["supply", supply],
            ["buy", buy],
            ["result", supply - buy]
        ]

        cvs_out = csv.writer(out_file, delimiter=",")
        cvs_out.writerows(report)
