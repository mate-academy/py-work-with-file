def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as f:
        data_list = f.readlines()
    supply = 0
    buy = 0
    for line in data_list:
        a = line.split(",")
        if a[0] == "supply":
            supply += int(a[1])
        if a[0] == "buy":
            buy += int(a[1])
    result = supply - buy
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
