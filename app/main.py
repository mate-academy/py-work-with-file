def create_report(data_file_name: str, report_file_name: str) -> None:
    unique_records = {"supply": 0, "buy": 0, }
    reports = ""
    with open(data_file_name, "r") as file:
        for line in file:
            action, quantity = line.strip().split(",")
            unique_records[action] += int(quantity)
    unique_records["result"] = unique_records["supply"] - unique_records["buy"]
    for key, value in unique_records.items():
        reports += key + "," + str(value) + "\n"

    with open(report_file_name, "w") as report:
        report.write(reports)
