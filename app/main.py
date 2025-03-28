from typing import Any


def create_report(data_file_name: str, report_file_name: str) -> Any:
    ffile = open(data_file_name, "r")
    lines = ffile.readlines()

    supply = 0
    buy = 0

    for line in lines:
        fixed_line = line.strip().split(",")
        operator, amount = fixed_line[0], int(fixed_line[1])
        if operator == "supply":
            supply += amount
        elif operator == "buy":
            buy += amount

    ffile.close()

    result = supply - buy

    new_file = open(report_file_name, "w")
    new_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
    new_file.close()
