import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supplies_num = 0
    purchases_num = 0

    with open(data_file_name, "r") as file_csv:
        csv_reader = csv.reader(file_csv)
        for row in csv_reader:
            if row:
                operation_type = row[0]
                amount = int(row[1])

                if operation_type == "supply":
                    supplies_num += amount
                elif operation_type == "buy":
                    purchases_num += amount

    result = supplies_num - purchases_num

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supplies_num}\n")
        report_file.write(f"buy,{purchases_num}\n")
        report_file.write(f"result,{result}\n")
