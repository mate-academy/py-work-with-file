def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, 'r') as data_file, \
            open(report_file_name, 'a') as report_file:
        data = data_file.read()
        list_data = data.split()
        supply = 0
        buy = 0
        for operation in list_data:
            if "buy" in operation:
                buy += int(operation.split(",")[1])
            else:
                supply += int(operation.split(",")[1])
        result = supply - buy

        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
