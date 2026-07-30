

def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_to_read:
        amount_supply = 0
        amount_buy = 0
        for line in file_to_read:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 2:
                raise ValueError(f"Invalid line format: {line}")

            operation_type, amount = parts

            try:
                if operation_type == "supply":
                    amount_supply += int(amount)
                elif operation_type == "buy":
                    amount_buy += int(amount)
            except ValueError:
                raise ValueError(f"Invalid amount value: {amount}")

    with open(report_file_name, "w") as file_to_write:
        file_to_write.write(f"supply,{amount_supply}\n")
        file_to_write.write(f"buy,{amount_buy}\n")
        result = amount_supply - amount_buy
        file_to_write.write(f"result,{result}\n")
