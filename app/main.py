def create_report(data_file_name: str, report_file_name: str) -> None:
    print(f"Function started with: {data_file_name}, {report_file_name}")
    with open(data_file_name, "r") as file:
        line = file.readlines()

    supply = 0
    buy = 0

    for lines in line[1:]:
        clean_line = lines.strip()
        if not clean_line:
            continue
        operation, amount = lines.strip().split(",")
        amount = int(amount)

        if operation == "supply":
            supply += amount
        if operation == "buy":
            buy += amount

    result = supply - buy
    print(result)

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")

    print(supply, buy, result)
