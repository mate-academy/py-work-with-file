def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    file_data = open(data_file_name, "r")
    for line in file_data:
        supply_or_buy = line.split(",")[0]
        quantity = int(line.split(",")[1])
        if supply_or_buy == "supply":
            supply += quantity
        else:
            buy += quantity
    result = supply - buy
    file_data.close()

    file_report = open(report_file_name, "w")
    file_report.write(f"supply,{supply}\n")
    file_report.write(f"buy,{buy}\n")
    file_report.write(f"result,{result}\n")
    file_report.close()
