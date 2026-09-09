def create_report(data_file_name: str,
                  report_file_name:str) -> None:
    with (open(data_file_name, "r") as data_file,
         open(report_file_name, "w") as report_file):
        values = {"supply": 0, "buy": 0}
        for line in data_file.readlines():
            key, num = line.strip().split(",")
            values[key] += int(num)
        report_file.write(f'supply,{values["supply"]}\n'
                          + f'buy,{values["buy"]}\n'
                          + f'result,{values["supply"] - values["buy"]}\n')
