def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            operation, amount_str = line.split(",")
            amount = int(amount_str)

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "w", encoding="utf-8") as outfile:
        outfile.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{result}\n"
        )
