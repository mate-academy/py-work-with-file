def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {
        "supply": 0,
        "buy": 0,
        "result": 0,
    }
    with open(data_file_name, "r") as from_file:
        for line in from_file.readlines():
            operation, amount = line.strip().split(",")
            result[operation] = result.get(operation, 0) + int(amount)

    result["result"] = result["supply"] - result["buy"]

    with open(report_file_name, "w") as in_file:
        for operation, amount in result.items():
            in_file.write(f"{operation},{amount}\n")
