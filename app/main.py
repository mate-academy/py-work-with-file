def create_report(data_file_name: str, report_file_name: str) -> str:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as in_file:
        for line in in_file:
            line = line.strip()
            parts = line.split(",")
            operation, amount = parts
            try:
                if operation == "supply":
                    supply += int(amount)
                elif operation == "buy":
                    buy += int(amount)
                else:
                    continue
            except ValueError:
                continue
        result = supply - buy
    with open(report_file_name, "w") as out_file:
        out_file.write(f"supply,{supply}\n")
        out_file.write(f"buy,{buy}\n")
        out_file.write(f"result,{result}\n")
