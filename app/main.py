import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    try:
        with open(data_file_name, "r", newline="", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            for row in reader:
                if not row:
                    continue

                if len(row) < 2:
                    print(f"Skipping malformed row: {row}")
                    continue

                operation_type = row[0].strip()
                try:
                    amount = int(row[1].strip())
                except ValueError:
                    print(f"Skipping row with invalid amount: {row}")
                    continue

                if operation_type == "supply":
                    total_supply += amount
                elif operation_type == "buy":
                    total_buy += amount
                else:
                    print(f"Skipping unknown operation type:"
                          f" {operation_type} in row: {row}")

    except FileNotFoundError:
        print(f"Error: Input file '{data_file_name}' not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return

    result = total_supply - total_buy

    try:
        with open(report_file_name,
                  "w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["supply", total_supply])
            writer.writerow(["buy", total_buy])
            writer.writerow(["result", result])
    except Exception as e:
        print(f"An error occurred while writing the report file: {e}")
