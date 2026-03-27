def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0
    with open(data_file_name, "r") as source:
        for line in source:
            new_line = line.split(",")
            if new_line[0] == "supply":
                supply += int(new_line[1])
            if new_line[0] == "buy":
                buy += int(new_line[1])
    with open(report_file_name, "a") as destination:
        destination.write("supply," + str(supply) + "\n")
        destination.write("buy," + str(buy) + "\n")
        destination.write("result," + str(supply - buy) + "\n")
