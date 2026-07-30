def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as file:
        lines = file.readlines()

    supply = 0
    buy = 0

    for line in lines:
        if not line.strip():
            continue
        operation, digit = line.strip().split(",")
        if operation == "buy":
            buy += int(digit)
        if operation == "supply":
            supply += int(digit)

    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")
