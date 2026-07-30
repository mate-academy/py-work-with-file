def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data:
        for information in data.readlines():
            action, value = tuple(information.split(","))
            if action == "buy":
                buy += int(value)
            if action == "supply":
                supply += int(value)

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
