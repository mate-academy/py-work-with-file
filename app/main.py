import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data = []
    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(tuple(row))

    supply = 0
    buy = 0
    for key, value in data:
        if key == "supply":
            supply += int(value)
        if key == "buy":
            buy += int(value)

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")

    with open(report_file_name, "a") as report_file:
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")
