def create_report(data_file_name: str, report_file_name: str) -> None:
    datas = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name, "r") as file_data:
        for line in file_data:
            if line:
                action, count = line.split(",")
                datas[action] += int(count)

    with open(report_file_name, "w") as report_file:
        for action, count in datas.items():
            report_file.write(f"{action},{datas[action]}\n")
        report_file.write(f"result,{datas['supply'] - datas['buy']}\n")
