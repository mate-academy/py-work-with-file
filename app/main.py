def create_report(data_file_name: str,
                  report_file_name: str
                  ) -> None:
    diction = {}
    with open(data_file_name, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            op, amount = line.split(",")
            op.strip()
            amount = int(amount.strip())
            diction[op] = diction.get(op, 0) + amount

    supply = diction.get("supply", 0)
    buy = diction.get("buy", 0)
    result = supply - buy
    with open(report_file_name, "w") as out:
        out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
