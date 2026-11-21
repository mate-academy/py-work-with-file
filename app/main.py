def create_report(data_file_name: str, report_file_name: str) -> str:
    data_file = {}

    for line in open(data_file_name):
        if line.split(",")[0] in data_file:
            data_file[line.split(",")[0]] += int(line.split(",")[1])
        else:
            data_file[line.split(",")[0]] = int(line.split(",")[1])

    report_file = open(report_file_name, "a")
    report_file.write(f'supply,{data_file["supply"]}\n')
    report_file.write(f'buy,{data_file["buy"]}\n')
    report_file.write(f'result,{data_file["supply"] - data_file["buy"]}\n')

    return open(report_file_name, "r").read()
