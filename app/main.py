def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as f:
        for line in f:
            if not line.strip():
                continue
            operation, amount = line.strip().split(",", 1)
            operation = operation.strip().lower()
            amount = amount.strip()
            try:
                value = int(amount)
            except ValueError:
                continue
            if operation == "supply":
                supply += value
            elif operation == "buy":
                buy += value

    result = supply - buy

    # Write the report in the required format
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
