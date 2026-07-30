def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_out:
        store_list = [i.replace("\n", "") for i in file_out.readlines()]
        supply = 0
        buy = 0
        for line in store_list:
            line_split = line.split(",")
            if line_split[0] == "supply":
                supply += int(line_split[1])
            if line_split[0] == "buy":
                buy += int(line_split[1])
        result = supply - buy
    with open(report_file_name, "w") as file_in:
        file_in.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
