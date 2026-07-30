import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    total_supply = 0
    total_buy = 0
    try:
        with open(data_file_name, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    operation_type, amount_str = row
                    try:
                        amount = int(amount_str)
                        if operation_type == "supply":
                            total_supply += amount
                        elif operation_type == "buy":
                            total_buy += amount
                    except ValueError:
                        print(f"Warning: Skipping invalid"
                              f" amount '{amount_str}' in row: {row}")
    except FileNotFoundError:
        print(f"Error: Input file '{data_file_name}' not found.")
        return

    result = total_supply - total_buy

    try:
        with open(report_file_name, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["supply", total_supply])
            writer.writerow(["buy", total_buy])
            writer.writerow(["result", result])
        print(f"Report successfully written to '{report_file_name}'")
    except IOError:
        print(f"Error: Could not write to report file '{report_file_name}'.")
