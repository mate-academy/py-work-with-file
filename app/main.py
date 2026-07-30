def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    result = 0
    with open(data_file_name, "r") as file:
        for line in file:
            action, quantity, *_ = line.split(",")
            if action == "buy":
                buy += int(quantity)
            if action == "supply":
                supply += int(quantity)
        result = supply - buy

    with open(report_file_name, "w") as file:
        file.write("supply," + f"{supply}\n")
        file.write("buy," + f"{buy}\n")
        file.write("result," + f"{result}\n")
