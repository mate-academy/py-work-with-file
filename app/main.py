def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    try:
        with open(data_file_name, "r", encoding="utf-8") as data_file:
            for line in data_file:
                line = line.strip()
                if not line:
                    continue
                try:
                    operation, amount = map(str.strip, line.split(",", 1))
                    amount = int(amount)
                except ValueError:
                    continue
                operation = operation.lower()
                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount
                else:
                    pass
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{data_file_name}' not found")
    result = supply - buy
    with open(report_file_name, "w", encoding="utf-8") as report_file:
        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{result}\n"
        )
