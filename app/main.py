def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    try:
        with open(data_file_name, "r") as data_file:
            for line in data_file:
                line = line.strip()
                if not line:
                    continue

                try:
                    operation, value_str = line.split(",")
                    value = int(value_str)
                except ValueError:
                    print(f"Invalid line skipped: '{line}'")
                    continue

                if operation == "supply":
                    supply_total += value
                elif operation == "buy":
                    buy_total += value
                else:
                    print(f"Unknown operation skipped: '{operation}'")

        result = supply_total - buy_total

        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{supply_total}\n")
            report_file.write(f"buy,{buy_total}\n")
            report_file.write(f"result,{result}\n")

    except FileNotFoundError:
        print(f"Error: File '{data_file_name}' not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as exc:
        print(f"Unexpected error: {exc}")

