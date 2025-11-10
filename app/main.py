def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    total = {}

    with open(data_file_name) as data_file:
        for line in data_file:
            operation, value = line.strip().split(",")
            value = int(value)

            if operation not in total:
                total[operation] = value
            else:
                total[operation] += value

    with open(report_file_name, "w") as report_file:
        report_file.write(f'supply,{total["supply"]}\n')
        report_file.write(f'buy,{total["buy"]}\n')
        report_file.write(f'result,{total["supply"] - total["buy"]}\n')
