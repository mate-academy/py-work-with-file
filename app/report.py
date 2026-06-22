import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        supply_total = 0
        buy_total = 0

        with open(data_file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                transaction_type = row[0].strip().lower()
                amount = int(row[1].strip())

                if transaction_type == "supply":
                    supply_total += amount
                elif transaction_type == "buy":
                    buy_total += amount

        result = supply_total - buy_total

        with open(report_file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["supply", supply_total])
            writer.writerow(["buy", buy_total])
            writer.writerow(["result", result])

        print(f"✓ Report created: {report_file_name}")

    except FileNotFoundError:
        print(f"✗ Error: File '{data_file_name}' not found")
    except (ValueError, IndexError) as e:
        print(f"✗ Error: Invalid CSV format - {e}")
    except IOError as e:
        print(f"✗ Error: Cannot write report - {e}")



