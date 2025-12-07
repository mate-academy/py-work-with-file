import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r", newline="") as data_file:
        reader = csv.reader(data_file)
        summary_suplies = 0
        summary_buyers = 0

        for row in reader:
            operation, amount = row[0], int(row[1])
            if operation == "supply":
                summary_suplies += amount
            elif operation == "buy":
                summary_buyers += amount
        result = summary_suplies - summary_buyers

    with open(report_file_name, "w", newline="") as report_file:
        report_file.write(f"supply,{summary_suplies}\n")
        report_file.write(f"buy,{summary_buyers}\n")
        report_file.write(f"result,{result}\n")
