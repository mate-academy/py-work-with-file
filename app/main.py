def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as in_file:
        operations = {}
        for line in in_file:
            operation, quantity = line.split(",")
            if operation not in operations:
                operations[operation] = 0
            operations[operation] += int(quantity)

    with open(report_file_name, "w") as out_file:
        out_file.write(f"supply,{operations['supply']}\n")
        out_file.write(f"buy,{operations['buy']}\n")
        out_file.write(f"result,{operations['supply'] - operations['buy']}\n")
