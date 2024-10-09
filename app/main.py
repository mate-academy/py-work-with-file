import os


def create_report(data_file_name: str, report_file_name: str) -> None:
    report_data = collect_data_from_csv(data_file_name)
    write_data_to_csv(report_file_name, report_data)


def collect_data_from_csv(file_name: str) -> dict:
    data = {}
    with open(file_name, "r") as data_file:
        for line in data_file:
            line_list = line.split(",")
            if data.get(line_list[0]):
                data[line_list[0]] += int(line_list[1])
            else:
                data[line_list[0]] = int(line_list[1])
        data["result"] = data.get("supply") - data.get("buy")
    return data


def write_data_to_csv(file_name: str, data: dict) -> None:
    with open(file_name, "w") as report_file:
        report_file.write(f"supply,{data.get("supply")}\n" # noqa E231
                          f"buy,{data.get("buy")}\n" # noqa E231
                          f"result,{data.get("result")}\n") # noqa E231
