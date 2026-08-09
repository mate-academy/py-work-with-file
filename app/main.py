def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Read supply/buy operations from a CSV file and write a summary
    report with total supply, total buy, and the resulting balance.

    :param data_file_name: str, path to the input CSV file. Each line
        contains "operation_type,amount" (e.g. "supply,30" or "buy,10").
        The last line may be empty and should be skipped.
    :param report_file_name: str, path to the output file where the
        report will be written.
    """
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()

            if not line:
                continue

            operation_type, amount = line.split(",")
            amount = int(amount)

            if operation_type == "supply":
                supply_total += amount
            elif operation_type == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
