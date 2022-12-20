from typing import Any


def create_report(date_file_name: str, report_file_name: str) -> Any:
    data_dict = {}
    with open(date_file_name, "r") as data:
        row = data.readline()
        while row != "":
            key, value = row.split(",")
            if key not in data_dict:
                data_dict[key] = int(value)
            else:
                data_dict[key] += int(value)
            row = data.readline()
    with open(report_file_name, "a") as report:
        result = 0
        for key, value in data_dict.items():
            report.write(f"{key},{value}\n")
            if key == "supply":
                result += value
            if key == "buy":
                result -= value
        report.write(f"result,{result}\n")
