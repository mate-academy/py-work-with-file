import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        with open(data_file_name, "r") as input_file:
            reader = csv.reader(input_file)
            rows = list(reader)

            supply_total = 0
            buy_total = 0

            for row in rows:
                if row and len(row) == 2:
                    operation, amount_str = row
                    try:
                        amount = int(amount_str)
                        if operation == "supply":
                            supply_total += amount
                        elif operation == "buy":
                            buy_total += amount
                    except ValueError:
                        pass

            result = supply_total - buy_total

            with open(report_file_name, "w") as output_file:
                writer = csv.writer(output_file)
                writer.writerow(["supply", str(supply_total)])
                writer.writerow(["buy", str(buy_total)])
                writer.writerow(["result", str(result)])
                print(f"Report has been created and saved to"
                      f" {report_file_name}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
