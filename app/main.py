def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f:
        for line in f:
            op_type, amount = line.strip().split(",")
            amount = int(amount)

            if op_type == "supply":
                supply += amount
            elif op_type == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
