def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source:
        lines = source.readlines()
        supply = 0
        buy = 0
        for line in lines:
            line_arr = line.strip("\n").split(",")
            if line_arr[0] == "buy":
                buy += int(line_arr[1])
            elif line_arr[0] == "supply":
                supply += int(line_arr[1])
        result = supply - buy
        with open(report_file_name, "w") as file_w:
            file_w.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
