def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0

    for line in open(data_file_name):
        if line.strip():
            operation, amount = line.split(",")
            if operation == "supply":
                supply += int(amount)
            if operation == "buy":
                buy += int(amount)

    result = supply - buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
