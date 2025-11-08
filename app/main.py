def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0
    input_file = open(data_file_name, "r")
    for line in input_file:
        line = line.strip()
        if not line:
            continue
        operation, amount = line.split(",")
        amount = int(amount)
        if operation == "supply":
            supply += amount
        elif operation == "buy":
            buy += amount
    input_file.close()
    result = supply - buy
    output_file = open(report_file_name, "w")
    output_file.write(f"supply,{supply}\n")
    output_file.write(f"buy,{buy}\n")
    output_file.write(f"result,{result}\n")
    output_file.close()
