def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(f"{data_file_name}", "r") as data_file:
        for line in data_file:
            column = line.split(",")
            if column[0] == "supply":
                supply += int(column[1])
            else:
                buy += int(column[1])

    result = supply - buy
    text = [
        f"supply,{str(supply)}\n"
        f"buy,{str(buy)}\n"
        f"result,{str(result)}\n"
    ]

    with open(f"{report_file_name}", "w") as report:
        report.writelines(text)
