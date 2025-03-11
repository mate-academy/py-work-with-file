def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, "r") as file:
        for line in file:
            st = line.split(",")
            if st[0] == "supply":
                supply_total += int(st[1])
            elif st[0] == "buy":
                buy_total += int(st[1])

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{supply_total - buy_total}\n")
