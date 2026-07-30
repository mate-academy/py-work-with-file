def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            operation, amount_str = line.split(",")
            amount = int(amount_str)
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

        result = supply - buy
        report_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{result}\n")
