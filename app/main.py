def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(f"{data_file_name}", "r") as file_in,\
            open(f"{report_file_name}", "a") as file_out:
        supply = 0
        buy = 0
        for line in file_in:
            splited_line = line.split(",")
            if splited_line[0] == "supply":
                supply += int(splited_line[1])
            elif splited_line[0] == "buy":
                buy += int(splited_line[1])
        result = supply - buy
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
