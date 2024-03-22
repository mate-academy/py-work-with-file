def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as new_file):

        report_file = data_file.readlines()
        report_dict = {"supply": 0, "buy": 0}

        for operation in report_file:
            type_operation, amount = operation.strip().split(",")
            report_dict[type_operation] += int(amount)

        result = report_dict["supply"] - report_dict["buy"]

        new_file.write(f"supply,{report_dict['supply']}\n")
        new_file.write(f"buy,{report_dict['buy']}\n")
        new_file.write(f"result,{result}\n")
