def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0
    with open(data_file_name, "r") as date_file:
        for line in date_file:
            name, count = line[:-1].split(",")
            if name == "supply":
                supply += int(count)
            else:
                buy += int(count)

    result = supply - buy
    with open(report_file_name, "w") as file:
        file.write("supply" + "," + f"{supply}\n")
        file.write("buy" + "," + f"{buy}\n")
        file.write("result" + "," + f"{result}\n")
