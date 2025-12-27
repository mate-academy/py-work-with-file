def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {
        "supply": 0,
        "buy": 0,
    }

    with open(data_file_name, "r") as file:
        file_date = file.readlines()

        for line in file_date:
            [operation, amount] = line.split(",")
            operations[operation] += int(amount)

    result = operations["supply"] - operations["buy"]
    with open(report_file_name, "w") as file:
        file.write(
            f'supply,{operations["supply"]}\nbuy,'
            f'{operations["buy"]}\nresult,{result}\n'
        )
