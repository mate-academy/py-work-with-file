def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    result = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        for line in file.readlines():
            divided_line = line.strip().split(",")

            operation_type = divided_line[0]
            amount = divided_line[1]

            if operation_type not in result:
                result[operation_type] = int(amount)
            else:
                result[operation_type] += int(amount)

    result["result"] = result.get("supply", 0) - result.get("buy", 0)

    with open(report_file_name, "w") as file:
        for operation_type, amount in result.items():
            file.write(operation_type
                       + ","
                       + str(amount)
                       + "\n")
