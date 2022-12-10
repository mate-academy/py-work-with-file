def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in, open(
        report_file_name, "w"
    ) as file_out:
        file_store_list = [
            file_line.replace("\n", "") for file_line in file_in.readlines()
        ]
        supply = 0
        buy = 0
        for line in file_store_list:
            line_list = line.split(",")
            if line_list[0] == "supply":
                supply += int(line_list[1])
            if line_list[0] == "buy":
                buy += int(line_list[1])
        result = supply - buy
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
