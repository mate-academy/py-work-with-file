def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        total_buy = sum(
            int(amount)
            for line in file
            if line.strip()
            for operation, amount in [line.strip().split(",")]
            if operation == "buy"
        )
        file.seek(0)
        total_supply = sum(
            int(amount)
            for line in file
            if line.strip()
            for operation, amount in [line.strip().split(",")]
            if operation == "supply"
        )
    with open(report_file_name, "w") as file:
        file.write(f"supply,{total_supply}\n")
        file.write(f"buy,{total_buy}\n")
        file.write(f"result,{total_supply - total_buy}\n")
