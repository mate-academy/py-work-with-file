def create_report(
        data_file_name: str,
        report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f:
        for line in f:
            operation, amount = line.strip().split(",")
            if operation == "supply":
                supply += int(amount)
            else:
                buy += int(amount)

    result = supply - buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
