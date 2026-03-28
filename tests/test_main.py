from __future__ import annotations
import csv


def create_file_from_input() -> None:
    filename = input("Enter name of the file: ").strip()
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(f"{filename}.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == "supply":
                supply_total += int(row[1])
            elif row[0] == "buy":
                buy_total += int(row[1])

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
