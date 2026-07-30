def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0
    with open(data_file_name, "r") as input_file:
        input_data = input_file.readlines()
        for lines in input_data:
            line = lines.strip().split(',')
            if line[0] == "supply":
                supply += int(line[1])
            elif line[0] == "buy":
                buy += int(line[1])

    with open(report_file_name, 'w') as report_file:
        report_file.writelines(f"supply,{supply}\n")
        report_file.writelines(f"buy,{buy}\n")
        report_file.writelines(f"result,{supply - buy}\n")
