def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    data = {"supply": 0, "buy": 0}

    for line in data_file.readlines():
        data_tup = line.split(",")
        data[data_tup[0]] += int(data_tup[1])

    data_file.close()

    report = open(report_file_name, "a")
    report.write(f'supply,{data["supply"]}\n'
                 f'buy,{data["buy"]}\n'
                 f'result,{data["supply"] - data["buy"]}\n')
    report.close()
