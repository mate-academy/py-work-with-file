def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data:
        data_dict = {}
        for line in data.readlines():
            key = line.split(",")[0]
            value = int(line.split(",")[1])
            if key in data_dict:
                data_dict[key] += value
            else:
                data_dict[key] = value
        data_dict["result"] = data_dict["supply"] - data_dict["buy"]
        with open(report_file_name, "a", newline="") as report:
            report.write(
                f'supply,{data_dict["supply"]}\n'
                f'buy,{data_dict["buy"]}\n'
                f'result,{data_dict["result"]}\n'
            )
