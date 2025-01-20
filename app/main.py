def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)
    buy = 0
    supply = 0
    for line in data_file:
        data_name, quantity = line.split(",")
        if data_name == "buy":
            buy += int(quantity.strip())
        elif data_name == "supply":
            supply += int(quantity.strip())
    data_file.close()

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
    report_file.close()
