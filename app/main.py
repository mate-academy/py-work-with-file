def create_report(data_file_name: str, report_file_name):
    operation_amount = {"buy": 0, "supply": 0}
    with open(data_file_name) as file1:
        for line in file1:
            info = line.strip('\n').split(',')
            operation_amount[info[0]] += int(info[1])
        with open(report_file_name, "w") as file2:
            supply = operation_amount["supply"]
            buy = operation_amount["buy"]
            result = supply - buy
            file2.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
