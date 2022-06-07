def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as data_file,\
         open(report_file_name, "w") as report_file:
        data = data_file.read().replace("\n", ",")
        data_ls = data.split(",")
        supply = 0
        buy = 0
        for i, d in enumerate(data_ls):
            if d == "supply":
                supply += int(data_ls[i + 1])
            elif d == "buy":
                buy += int(data_ls[i + 1])
        result = supply - buy
        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
