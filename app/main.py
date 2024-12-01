def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    file1 = open(data_file_name, "r")
    for line in file1:
        line = line.strip()
        if not line:
            continue

        operation, amount = line.split(",")
        amount = int(amount)

        if operation == "supply":
            supply += amount
        elif operation == "buy":
            buy += amount

    file1.close()

    result = supply - buy

    file2 = open(report_file_name, "w")
    file2.write("supply,"f"{supply}\n")
    file2.write("buy,"f"{buy}\n")
    file2.write("result,"f"{result}\n")
    file2.close()
