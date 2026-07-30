import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row and row[0] in ("supply", "buy"):  # Check for empty lines
                operation_type, amount = row
                amount = int(amount)
                if operation_type == "supply":
                    supply += amount
                elif operation_type == "buy":
                    buy += amount

    result = supply - buy

    with open(report_file_name, "w") as reportfile:
        reportfile.write(f"supply,{supply}\n")
        reportfile.write(f"buy,{buy}\n")
        reportfile.write(f"result,{result}\n")

    print(f"Report generated successfully and saved to {report_file_name}")
