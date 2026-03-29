import os


def create_report(data_file_name: str, report_file_name: str) -> None:
    datas = {
        "supply": 0,
        "buy": 0
    }

    with open(
            os.path.join("", data_file_name),
            "r"
    ) as data_file:
        for line in data_file:
            if line:
                command, value = line.split(",")
                datas[command] += int(value)

    with open(os.path.join("", report_file_name), "w") as report_file:
        for command, value in datas.items():
            report_file.write(f"{command},{value}\n")
        report_file.write(f"result,{datas['supply'] - datas['buy']}\n")
