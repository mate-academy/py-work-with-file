def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_total = 0
    supply_total = 0

    with open(data_file_name, "r") as source_file:
        for line in source_file.readlines():
            data = line.split(",")
            if data[0] == "buy":
                buy_total += int(data[1])
            elif data[0] == "supply":
                supply_total += int(data[1])

    result = supply_total - buy_total

    with open(report_file_name, "a") as result_file:
        result_file.write(f"supply,{supply_total}\n")
        result_file.write(f"buy,{buy_total}\n")
        result_file.write(f"result,{result}\n")
