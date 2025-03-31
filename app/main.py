def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {'supply': 0, 'buy': 0, 'result': 0}
    with open(data_file_name, 'r') as f:
        for line in f:
            formated_line = line.split(',')
            report[formated_line[0]] += int(formated_line[1])

    report['result'] = report['supply'] - report['buy']

    with open(report_file_name, 'w') as rep:
        rep.write(f"supply,{report['supply']}\n")
        rep.write(f"buy,{report['buy']}\n")
        rep.write(f"result,{report['result']}\n")

    rep.close()
    f.close()
