def create_report(data_file_name: str, report_file_name: str) -> None:
    file = open("../" + data_file_name)

    supply = 0
    buy = 0
    for line in file:
        data = line.split(",")
        if data[0] == "supply":
            supply += int(data[1])
        elif data[0] == "buy":
            buy += int(data[1])

    file.close()

    report_file = open(report_file_name, 'w')
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")



