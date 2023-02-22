def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_1, \
         open(report_file_name, "w") as file_2:
        buy = []
        supply = []
        for line in file_1.readlines():
            data_line = line.split(",")
            if data_line[0] == "supply":
                supply.append(int(data_line[1]))
            elif data_line[0] == "buy":
                buy.append(int(data_line[1]))
        result = sum(supply) - sum(buy)
        report = f"supply,{sum(supply)}\nbuy,{sum(buy)}\nresult,{result}\n"
        file_2.write(report)
