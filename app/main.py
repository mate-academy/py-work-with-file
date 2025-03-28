def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}

    with (open(data_file_name, "r") as old_data,
          open(report_file_name, "w") as report):

        for string in old_data:
            if string:
                operation_type, amount = map(str.strip, string.split(","))
                data[operation_type] += int(amount)

        report.write(f'supply,{data["supply"]}\n') # noqa
        report.write(f'buy,{data["buy"]}\n') # noqa
        report.write(f'result,{data["supply"] - data["buy"]}\n') # noqa
