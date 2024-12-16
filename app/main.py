def create_report(data_file_name: str, report_file_name: str) -> None:
    report_file = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    with open(data_file_name, "r") as file:
        for line in file.readlines():
            if line:
                key, value = line.split(",")
                report_file[key] += int(value)

        report_file["result"] = report_file["supply"] - report_file["buy"]

    with open(report_file_name, "w") as file:
        for key, value in report_file.items():
            file.write(f"{key},{value}\n")
