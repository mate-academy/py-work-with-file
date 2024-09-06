def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open("../" + data_file_name)

    supply = 0
    buy = 0
    for line in data_file:
        data = line.split(",")
        if data[0] == "supply":
            supply += int(data[1])
        elif data[0] == "buy":
            buy += int(data[1])

    data_file.close()

    report_file = open(report_file_name, "w")
    report_file.write("supply,")
    report_file.write(f"{supply}\n")
    report_file.write("buy,")
    report_file.write(f"{buy}\n")
    report_file.write("result,")
    report_file.write(f"{supply - buy}\n")
