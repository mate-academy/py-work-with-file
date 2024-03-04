def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {}
    with open(data_file_name, "r") as source:
        while line := source.readline():
            key, val = line.split(",")
            if key not in data:
                data[key] = int(val)
            else:
                data[key] += int(val)
    data["result"] = data["supply"] - data["buy"]

    with open(report_file_name, "w") as target:
        target.write(f'supply,{data["supply"]}\n')
        target.write(f'buy,{data["buy"]}\n')
        target.write(f'result,{data["result"]}\n')
