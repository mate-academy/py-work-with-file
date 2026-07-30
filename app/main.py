def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0
    with open(data_file_name, "r") as file_in,\
            open(report_file_name, "w") as file_out:
        for line in file_in:
            line_list = line.split(",")
            if line_list[0] == "supply":
                supply += int(line_list[1])
            if line_list[0] == "buy":
                buy += int(line_list[1])
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
