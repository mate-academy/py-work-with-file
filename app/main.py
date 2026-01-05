def create_report(data_file_name: str, report_file_name: str) -> None:
    f1 = open("../" + data_file_name, "r")

    supply = 0
    buy = 0

    for line in f1:
        split_line = line.split(",")
        if split_line[0] == "supply":
            supply += int(split_line[1].strip("\n"))
        if split_line[0] == "buy":
            buy += int(split_line[1].strip("\n"))

    f2 = open(report_file_name, "w")
    f2.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
    f2.close()

    f1.close()
