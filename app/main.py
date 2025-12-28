def create_report(data_file_name: str, report_file_name: str) -> None:

    report_list = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            key, value = line.split(",")
            value = int(value.split()[0])
            report_list[key] += value

    report_list["result"] = report_list["supply"] - report_list["buy"]

    with open(report_file_name, "w") as report_file:
        for title, value in report_list.items():
            report_file.write(f"{title},{value}\n")
