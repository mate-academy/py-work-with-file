def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            temp = line.strip().split(",")
            if temp[0] == "buy":
                buy += int(temp[1])
            elif temp[0] == "supply":
                supply += int(temp[1])

    with open(report_file_name, "w") as file:
        file.write("supply," + f"{supply}\n")
        file.write("buy," + f"{buy}\n")
        file.write("result," + f"{supply - buy}\n")
