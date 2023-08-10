def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):

        data_ = file_in.read().splitlines()

        report = {"supply": 0, "buy": 0}

        for operation in data_:
            operation_type, amount = operation.split(",")
            report[operation_type] += int(amount)

        file_out.write(f"supply,{report['supply']}\n"
                       f"buy,{report['buy']}\n"
                       f"result,{report['supply'] - report['buy']}\n")
