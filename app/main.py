def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        with open(data_file_name, "r") as f:
            lines = f.readlines()

        total_supply = 0
        total_buy = 0

        for line in lines:
            if line.strip():  # Check if the line is not empty
                operation_type, amount = line.strip().split(",")
                amount = int(amount)

                if operation_type == "supply":
                    total_supply += amount
                elif operation_type == "buy":
                    total_buy += amount

        total_result = total_supply - total_buy

        with open(report_file_name, "w") as write_file:
            write_file.write(f"supply,{total_supply}\n")
            write_file.write(f"buy,{total_buy}\n")
            write_file.write(f"result,{total_result}\n")

    except FileNotFoundError:
        pass
    except ValueError:
        pass
