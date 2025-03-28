def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {}
    with (open(data_file_name, "r") as input_data,
          open(report_file_name, "w") as report_data):
        for line in input_data:
            if line:
                line = line.split(",")
            data[line[0]] = data.get(line[0], 0) + int(line[1])
        report_data.write(f'supply,{data["supply"]}\n')
        report_data.write(f'buy,{data["buy"]}\n')
        report_data.write(f'result,{data["supply"] - data["buy"]}\n')
