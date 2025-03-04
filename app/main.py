def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as d_f:
        for line in d_f:
            operation, amount = line.split(",")
            amount = int(amount)
            if operation == "supply":
                supply += amount
            if operation == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "a") as r_f:
        r_f.write(f"supply,{supply}\n")
        r_f.write(f"buy,{buy}\n")
        r_f.write(f"result,{result}\n")
