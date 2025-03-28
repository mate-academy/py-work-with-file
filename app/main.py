import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0

    with open(data_file_name, "r") as input_file:
        csv_reader = csv.reader(input_file)
        for row in csv_reader:
            if len(row) == 2:
                operation, amount = row
                amount = int(amount)
                if operation == "supply":
                    supply_sum += amount
                elif operation == "buy":
                    buy_sum += amount

    result = supply_sum - buy_sum

    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{supply_sum}\n")
        output_file.write(f"buy,{buy_sum}\n")
        output_file.write(f"result,{result}\n")
