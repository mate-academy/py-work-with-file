def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as source:
        for line in source:
            if not line:
                break
            operation_type, amount = line.split(",")
            operations[operation_type] += int(amount)
    operations["result"] = operations["supply"] - operations["buy"]

    with open(report_file_name, "w") as target:
        target.write("".join([
            f"{key},{value}\n" for key, value in operations.items()
        ]))
