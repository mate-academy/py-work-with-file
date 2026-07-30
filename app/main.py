# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)
    supply = 0
    buy = 0

    for line in data_file:
        elems = line.split(",")
        if elems[0] == "supply":
            supply += int(elems[1])
        else:
            buy += int(elems[1])
    data_file.close()

    report = open(report_file_name, "w")
    report.write("supply," + str(supply) + "\n")
    report.write("buy," + str(buy) + "\n")
    report.write("result," + str(supply - buy) + "\n")
    report.close()
