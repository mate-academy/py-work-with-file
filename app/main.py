def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0
    with (open(data_file_name, "r") as data,
          open(report_file_name, "w") as report):
        for line in data:
            splitted = line.split(",")
            if splitted[0] == "supply":
                supply += int(splitted[1])
            elif splitted[0] == "buy":
                buy += int(splitted[1])
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
