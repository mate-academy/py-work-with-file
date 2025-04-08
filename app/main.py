def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name) as f:
        for line in f:
            if line.strip():
                op, amount = line.strip().split(',')
                if op == "supply":
                    supply += int(amount)
                elif op == "buy":
                    buy += int(amount)

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{supply - buy}\n")
