def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supplies = 0
    total_buys = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            operation, value = line.split(",")
            value = int(value)
            if operation == "supply":
                total_supplies += value
            elif operation == "buy":
                total_buys += value

    total_result = total_supplies - total_buys

    with open(report_file_name, "w") as file:
        file.write(f"supply,{total_supplies}\n")
        file.write(f"buy,{total_buys}\n")
        file.write(f"result,{total_result}\n")
