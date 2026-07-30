def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        parts = line.split(",")
        operation = parts[0]
        amount = int(parts[1])

        if operation == "supply":
            supply += amount
        elif operation == "buy":
            buy += amount

    result = supply - buy

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
