def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {}
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            split = line.split(",")
            operation_type = split[0]
            amount = int(split[1].strip())
            if operation_type not in operations.keys():
                operations[operation_type] = amount
            else:
                operations[operation_type] += amount

    operations["result"] = operations["supply"] - operations["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write(f'supply,{operations["supply"] }\n')
        report_file.write(f'buy,{operations["buy"]}\n')
        report_file.write(f'result,{operations["result"]}\n')
