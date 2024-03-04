def create_report(data_file_name: str, report_file_name: str) -> None:
    storage = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data:
        for line in data.readlines():
            operation = line.split(",")
            storage[operation[0]] += int(operation[1])
    with open(report_file_name, "w") as report:
        report.write(f'supply,{storage.get("supply")}\n'
                     f'buy,{storage.get("buy")}\n'
                     f'result,{storage.get("supply") - storage.get("buy")}\n')
