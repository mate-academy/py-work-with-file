def create_report(data_file_name: str, report_file_name: str) -> str:
    fl = open(data_file_name)

    supply = 0
    buy = 0
    for line in fl:
        item, count = line.split(",")
        if item == "supply":
            supply += int(count[:-1])
        else:
            buy += int(count[:-1])
    fl.close()

    fl = open(report_file_name, "w")
    fl.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
    fl.close()
