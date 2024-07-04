def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    opend_file = open(data_file_name, "r")

    for line in opend_file:
        parts = line.strip().split(",")

        operation_type = parts[0].strip().lower()
        amount = float(parts[1].strip())

        if operation_type == "supply":
            supply += amount
        elif operation_type == "buy":
            buy += amount

    result = supply - buy

    report_file = open(report_file_name, "w")

    report_file.write(f"supply,{int(supply)}\n")
    report_file.write(f"buy,{int(buy)}\n")
    report_file.write(f"result,{int(result)}\n")

    opend_file.close()
    report_file.close()
