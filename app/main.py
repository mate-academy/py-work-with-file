def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0

    with open(data_file_name, "r") as f:
        for data in f.readlines():
            if not data:
                continue

            operation, amount = data.split(",")

            if operation == "supply":
                supply += int(amount)
            if operation == "buy":
                buy += int(amount)

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{supply - buy}\n")
