def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            op = parts[0].strip()
            amount = int(parts[1].strip())
            if op == "buy":
                buy += amount
            elif op == "supply":
                supply += amount

    result = supply - buy

    with open(report_file_name, "w") as out:
        out.writelines(
            [f"supply,{supply}\n", f"buy,{buy}\n", f"result,{result}\n"]
        )
