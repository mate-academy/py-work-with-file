from typing import TextIO


def create_report(data_file_name: str, report_file_name: str) -> TextIO:
    supply = 0
    buy = 0
    file_data = open(f"../{data_file_name}", "r")
    for line in file_data:
        splited_line = line.split(",")
        if splited_line[0] == "buy":
            buy += int(splited_line[1])
        if splited_line[0] == "supply":
            supply += int(splited_line[1])
    result = supply - buy
    with open(report_file_name, "w") as new_file:
        new_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")

    return new_file
