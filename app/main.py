def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    data_f = open(data_file_name, "r")
    data_stat = {}

    for line in data_f:
        row = line.replace("\n", "").split(",")
        # print(row[0], row[1])
        if row[0] in data_stat:
            data_stat[row[0]] += int(row[1])
        else:
            data_stat[row[0]] = int(row[1])

    data_stat["result"] = data_stat["supply"] - data_stat["buy"]
    report_list = (f'supply,{data_stat["supply"]}\n'
                   f'buy,{data_stat["buy"]}\n'
                   f'result,{data_stat["result"]}\n')
    report_f = open(report_file_name, "w")

    report_f.write(report_list)
    data_f.close()
    report_f.close()
