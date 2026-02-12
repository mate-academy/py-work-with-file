def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply_total = 0
    buy_total = 0

    for line in data_file.readlines():
        index = line.index(",")
        key = line[0:index]
        value = line[index + 1: -1]
        if key == "supply":
            supply_total += int(value)
        elif key == "buy":
            buy_total += int(value)

    new_file = open(report_file_name, "a")
    new_file.write(
        f"supply,{supply_total}\n"
        f"buy,{buy_total}\n"
        f"result,{supply_total - buy_total}\n"
    )
    data_file.close()
    new_file.close()
