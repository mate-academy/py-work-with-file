def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0
    with open(data_file_name, "r") as r_file:
        for line in r_file:
            temp_line = line.split(",")
            if temp_line[0] == "supply":
                supply += int(temp_line[1])
            if temp_line[0] == "buy":
                buy += int(temp_line[1])
    with open(report_file_name, "w") as w_file:
        w_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
