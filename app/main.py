def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            cmd, amount_str = line.split(",")
            amount = int(amount_str)
            if cmd == "supply":
                supply += amount
            elif cmd == "buy":
                buy += amount

    with open(report_file_name, "w") as result:
        result.write(f"supply,{supply}\n")
        result.write(f"buy,{buy}\n")
        result.write(f"result,{supply - buy}\n")
