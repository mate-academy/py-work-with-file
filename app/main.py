import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, newline="") as input_file:
        reader = csv.reader(input_file)
        data = list(reader)
        print(data)
    buy = 0
    supply = 0
    for el in data:
        if el[0] == "buy":
            buy += int(el[1])
        else:
            supply += int(el[1])

    with open(report_file_name, "w") as report:
        report.write(
            f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
