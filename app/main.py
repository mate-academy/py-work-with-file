def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply = 0
    buy = 0
    result = 0

    for line in data_file.readlines():
        name, price = line.split(",")

        if name == "buy":
            buy += int(price)
        if name == "supply":
            supply += int(price)
    result = supply - buy
    print(supply, buy, result)
    data_file.close()

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}")
    report_file.close()
