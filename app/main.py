def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        x = file.read().split("\n")
        for i in x:
            if "supply" in i:
                supply += int(i[7:])
            elif "buy" in i:
                buy += int(i[4:])
    result = supply - buy
    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
