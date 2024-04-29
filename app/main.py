def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as d, open(report_file_name, "w") as f:
        for line in d.readlines():
            data = line.split(",")
            if data[0] == "supply":
                supply += int(data[1][:-1])
            elif data[0] == "buy":
                buy += int(data[1][:-1])
        result = supply - buy
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
