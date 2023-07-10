def create_report(data_file_name: str,
                  report_file_name: str) -> None:

    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file.readline():
            item, quantity = line.split(",")
            if item == "supply":
                supply += quantity
            if item == "buy":
                buy += quantity

    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(supply) + "\n"
                          + "buy," + str(buy) + "\n"
                          + "result," + str(supply - buy) + "\n")
