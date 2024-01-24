def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}

    with (open(data_file_name, "r") as input_csv_data,
          open(report_file_name, "w") as report_csv_data):
        for line in input_csv_data:
            if line:
                transaction_type, quantity = map(str.strip, line.split(","))
                data[transaction_type] += int(quantity)

        report_csv_data.write(f'supply,{data["supply"]}\n')
        report_csv_data.write(f'buy,{data["buy"]}\n')
        report_csv_data.write(f'result,{data["supply"] - data["buy"]}\n')
