def create_report(data_file_name: str, report_file_name: str) -> None:
    def read_lines_ignoring_last_empty(filename: str) -> list:
        with open(filename, "r") as file:
            lines = file.readlines()
            if lines and lines[-1].strip() == "":
                lines.pop()
        return lines

    lines = read_lines_ignoring_last_empty(data_file_name)

    total_supply = 0
    total_buy = 0

    for line in lines:
        operation, amount = line.strip().split(",")
        amount = int(amount)
        if operation == "supply":
            total_supply += amount
        elif operation == "buy":
            total_buy += amount

    result = total_supply - total_buy

    report_lines = [
        f"supply, {total_supply}",
        f"buy, {total_buy}",
        f"result, {result}"
    ]

    with open(report_file_name, "w") as report_file:
        for report_line in report_lines:
            report_file.write(report_line.replace(" ", "") + "\n")
