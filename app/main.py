def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    try:
        with open(data_file_name, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) < 2:
                    continue

                operation_type = parts[0].strip()
                try:
                    amount = int(parts[1].strip())
                except ValueError:
                    continue

                if operation_type == "supply":
                    total_supply += amount
                elif operation_type == "buy":
                    total_buy += amount
    except FileNotFoundError:
        print(f"Error: File {data_file_name} not found")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    result = total_supply - total_buy

    try:
        with open(report_file_name, "w") as file_report:
            file_report.write(
                f"supply,{total_supply}\n"
                f"buy,{total_buy}\n"
                f"result,{result}\n"
            )
    except Exception as e:
        print(f"Error writing report file: {e}")
