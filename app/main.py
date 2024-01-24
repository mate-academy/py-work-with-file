def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}

    with (open(data_file_name, "r") as inputer,
          open(report_file_name, "w") as report):
        for line in inputer:
            if line:
                transaction_type, quantity = map(str.strip, line.split(","))
                data[transaction_type] += int(quantity)

        report.write(f'supply,{data["supply"]}\n')
        report.write(f'buy,{data["buy"]}\n')
        report.write(f'result,{data["supply"] - data["buy"]}\n')
