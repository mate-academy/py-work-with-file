def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as input_file:
        for line in input_file.readlines():
            if len(line) > 1:
                operation, amount = line.split(",")
                operations[operation] += int(amount)

    operations["result"] = operations.get("supply") - operations.get("buy")
    with open(report_file_name, "w") as output_file:
        for key, value in operations.items():
            output_file.write(f"{key},{value}\n")
