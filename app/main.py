def create_report(data_file_name, report_file_name):
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data, \
            open(report_file_name, "w") as report:
        for line in data.readlines():
            list_info = line.split(",")
            if list_info[0] == "supply":
                supply += int(list_info[1])
            else:
                buy += int(list_info[1])
        result = supply - buy
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
