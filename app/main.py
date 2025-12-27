def create_report(data_file_name: str, report_file_name: str) -> None:
    file_date = open(data_file_name, "r").readlines()

    operations = {
        "supply": 0,
        "buy": 0,
    }

    for line in file_date:
        [operation, amount] = line.split(",")
        operations[operation] += int(amount)

    result = operations["supply"] - operations["buy"]
    open(report_file_name, "w").write(
        f'supply,{operations["supply"]}\nbuy,'
        f'{operations["buy"]}\nresult,{result}\n'
    )
