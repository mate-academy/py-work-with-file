from typing import Any


def create_report(date_file_name: str, report_file_name: str) -> Any:
    data_dict = {}
    with open(date_file_name, "r") as data,\
            open(report_file_name, "a") as report:
        row = data.readline()
        while row != "":
            key, value = row.split(",")
            if key not in data_dict:
                data_dict[key] = int(value)
            else:
                data_dict[key] += int(value)
            row = data.readline()
        result = data_dict["supply"] - data_dict["buy"]
        report.write(f"supply,{data_dict['supply']}\n"
                     f"buy,{data_dict['buy']}\nresult,{result}\n")
