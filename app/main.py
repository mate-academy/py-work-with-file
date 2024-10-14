def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        data = f.read().split("\n")[:-1]
        supply, buy = 0, 0
        for item in data:
            item = item.split(",")
            if item[0] == "supply":
                supply += int(item[1])
            elif item[0] == "buy":
                buy += int(item[1])

    with open(report_file_name, "w") as f:
        f.write("supply," + str(supply) + "\n")
        f.write("buy," + str(buy) + "\n")
        f.write("result," + str(supply - buy) + "\n")
