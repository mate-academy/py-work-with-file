def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as r_file:
        supply = 0
        buy = 0
        for line in r_file:
            if not line.strip():
                continue
            line_list = line.strip().split(",")
            amount = int(line_list[1])
            if line_list[0] == "supply":
                supply += amount
            if line_list[0] == "buy":
                buy += amount
        result = supply - buy
    with open(report_file_name, "w") as w_file:
        w_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
