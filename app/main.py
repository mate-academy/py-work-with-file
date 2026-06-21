def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f:
        for line in f:
            list_of_line = line.split(",")
            if not line:
                continue
            elif list_of_line[0] == "buy":
                buy += int(list_of_line[1])
            elif list_of_line[0] == "supply":
                supply += int(list_of_line[1])
    result = supply - buy
    with open(report_file_name, "w") as r:
        r.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
