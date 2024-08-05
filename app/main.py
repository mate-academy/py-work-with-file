def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}

    file_to_read = open(data_file_name)

    for string in file_to_read:
        if string:
            operation_type, amount = string.split(",")
            if operation_type == "supply":
                data["supply"] += int(amount)
            else:
                data["buy"] += int(amount)

    file_to_read.close()

    with open(report_file_name, "a") as report:

        report.write(f"supply,{data["supply"]}\n")
        report.write(f"buy,{data["buy"]}\n")
        report.write(f"result,{data["supply"] - data["buy"]}\n")
