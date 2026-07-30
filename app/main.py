def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file_info:
        for row in file_info:
            if row.split(",")[0] == "supply":
                supply += int(row.split(",")[1])
            if row.split(",")[0] == "buy":
                buy += int(row.split(",")[1])

    result = supply - buy

    with open(report_file_name, "w") as file_report:
        file_report.write(f"supply,{supply}\n")
        file_report.write(f"buy,{buy}\n")
        file_report.write(f"result,{result}\n")
