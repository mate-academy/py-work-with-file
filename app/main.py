import csv

def main(data_file_name: str, report_file_name: str) -> None:
    """Reads a CSV file, processes supply and buy operations, and writes a report."""
    supply_total: int = 0
    buy_total: int = 0

    # Read data from CSV file
    with open(data_file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:  # Ensure the row has two elements
                operation, amount = row
                if operation == "supply":
                    supply_total += int(amount)
                elif operation == "buy":
                    buy_total += int(amount)

    # Calculate result
    result: int = supply_total - buy_total

    # Write report to new file
    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")
