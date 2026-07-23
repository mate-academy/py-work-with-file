def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()

            if not clean_line:
                continue

            try:
                operation, amount = clean_line.split(",")
                operation = operation.strip()
                amount = int(amount.strip())
            except ValueError:
                continue

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "w", encoding="utf-8") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")


if __name__ == "__main__":
    create_report("apples.csv", "apples_report.csv")
