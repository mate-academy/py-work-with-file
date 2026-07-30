def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {'supply': 0, 'buy': 0, 'result': 0}
    with open(data_file_name, 'r') as f_data:
        while True:
            line = f_data.readline().split(',')
            if line[0] == '':
                break
            report[line[0]] += int(line[1])

    report['result'] = report['supply'] - report['buy']

    with open(report_file_name, 'w') as f_report:
        for key, value in report.items():
            print(f'{key},{value}', file=f_report)
