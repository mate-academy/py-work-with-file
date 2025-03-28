import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        with (open(data_file_name, "r") as data_file,
              open(report_file_name, "w", newline="") as report_file):
            reader = csv.reader(data_file)
            writer = csv.writer(report_file)

            supply = 0
            buy = 0

            for row in reader:
                if row:
                    operation_type, amount = row
                    amount = int(amount)

                    if operation_type == "supply":
                        supply += amount
                    elif operation_type == "buy":
                        buy += amount

            result = supply - buy
            writer.writerow(["supply", supply])
            writer.writerow(["buy", buy])
            writer.writerow(["result", result])

        print(f"Report created successfully."
              f" Check {report_file_name} for the report.")

    except Exception as e:
        print(f"An error occurred: {e}")
