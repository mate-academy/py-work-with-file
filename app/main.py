def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, 'r') as data_file:
        supply = 0
        buy = 0
        for line in data_file:
            line = line.split(',')
            if line[0] == 'supply':
                supply += int(line[1])
            if line[0] == 'buy':
                buy += int(line[1])

        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{supply}\n"
                              f"buy,{buy}\n"
                              f"result,{supply - buy}\n")
