import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)
        supply_total = 0
        buy_total = 0

        for row in csv_reader:
            # Check if the row is not empty
            if row:
                operation_type, amount_str = row
                amount = int(amount_str)

                if operation_type == "supply":
                    supply_total += amount
                elif operation_type == "buy":
                    buy_total += amount

        result = supply_total - buy_total

        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{supply_total}\n")
            report_file.write(f"buy,{buy_total}\n")
            report_file.write(f"result,{result}\n")
