def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0

    with open(data_file_name, 'r') as f:
        for line in f:
            line_lst = line.split(',')

            if line_lst[0] == 'supply':
                supply += int(line_lst[1])

            elif line_lst[0] == 'buy':
                buy += int(line_lst[1])

    with open(report_file_name, 'w') as f:
        report = f'supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n'

        f.write(report)
