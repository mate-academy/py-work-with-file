import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    try:
        with open(data_file_name, mode="r", newline="") as data_file:
            reader = csv.reader(data_file)
            for row in reader:
                if not row:
                    continue
                if len(row) != 2:
                    print(f"Invalid row skipped: {row}")
                    continue

                operation, value_str = row
                try:
                    value = int(value_str)
                except ValueError:
                    print(f"Invalid value skipped: {value_str}")
                    continue

                if operation == "supply":
                    supply_total += value
                elif operation == "buy":
                    buy_total += value
                else:
                    print(f"Unknown operation skipped: '{operation}'")

        result = supply_total - buy_total

        with open(report_file_name, mode="w", newline="") as report_file:
            writer = csv.writer(report_file)
            writer.writerow(["supply", supply_total])
            writer.writerow(["buy", buy_total])
            writer.writerow(["result", result])

    except FileNotFoundError:
        print(f"Error: File '{data_file_name}' not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as exc:
        print(f"Unexpected error: {exc}")
