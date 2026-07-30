def create_report(data_file_name: str, report_file_name: str) -> None:
    file_data = open(data_file_name)
    data_set = file_data.readlines()
    supply = 0
    buy = 0
    for data in data_set:
        array = data.split(",")
        if array[0] == "supply":
            supply += int(array[1])
        if array[0] == "buy":
            buy += int(array[1])

    result = supply - buy
    content = f"supply,{str(supply)}\nbuy,{str(buy)}\nresult,{result}\n"
    report = open(report_file_name, "w")
    report.write(content)
