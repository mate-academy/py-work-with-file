def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        for line in file:
            if not line.strip():
                continue

            operation, value = line.strip().split(",")
            value = int(value)

            if operation in operations:
                operations[operation] += value

    result = operations["supply"] - operations["buy"]

    with open(report_file_name, "w") as file:
        file.write(f"supply,{operations['supply']}\n")
        file.write(f"buy,{operations['buy']}\n")
        file.write(f"result,{result}\n")
