def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, "r") as file1:

        for line in file1.readlines():
            row = line.split(",")
            if row[0] == "supply":
                supply_total += int(row[1])
            elif row[0] == "buy":
                buy_total += int(row[1])

    result = supply_total - buy_total

    with open(report_file_name, "w") as file2:
        file2.write(f"supply,{supply_total}\n")
        file2.write(f"buy,{buy_total}\n")
        file2.write(f"result,{result}\n")
