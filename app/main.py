def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0

    with open(data_file_name, "r") as data:
        copy = data.read()
        copy = copy.split()
        for pair in copy:
            pair = pair.split(",")
            if pair[0] == "supply":
                supply += int(pair[1])
            else:
                buy += int(pair[1])

    with open(report_file_name, "a") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
