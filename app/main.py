def create_report(data_file_name: str, report_file_name: str) -> None:
    info = {
        "supply": int(0),
        "buy": int(0),
        "result": int(0)
    }

    with open(data_file_name) as file:
        for line in file.readlines():
            key, value = line.split(",")
            value = int(value)
            info[key] += value

    with open(report_file_name, "w") as file:
        file.write(f'supply, {info["supply"]}\n')
        file.write(f'buy, {info["buy"]}\n')
        file.write(f'result, {info["supply"] - info["buy"]}\n')
