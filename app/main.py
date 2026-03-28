def create_report(
        data_file_name: str,
        report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data:
        for dt in data:
            splited = dt.split(",")
            content = splited[0]
            quantity = int(splited[1])
            if "supply" == content:
                supply += quantity
            else:
                buy += quantity
    result = supply - buy
    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
