def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        lines = f.read().split("\n")

    result = {}
    for line in lines:
        operation_type, amount = line.split(",")
        if operation_type in result:
            result[operation_type] += amount
        else:
            result[operation_type] = amount

    with open(report_file_name, "w") as f:
        for operation_type, amount in result.items():
            f.write(str(operation_type, amount))
