import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {}

    with open(data_file_name, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                operation_type, amount = row
                if operation_type not in data:
                    data[operation_type] = 0
                data[operation_type] += int(amount)

    supply_total = data.get("supply", 0)
    buy_total = data.get("buy", 0)
    result = supply_total - buy_total

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")


if __name__ == "__main__":
    data_file_name = input("Enter the name of the input CSV file: ")
    report_file_name = input("Enter the name of the output report file: ")
    create_report(data_file_name, report_file_name)
