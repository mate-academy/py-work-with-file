def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total, buy_total = 0, 0

    with open(data_file_name) as in_file:
        for line in in_file:
            if line.strip():
                action, amount = line.strip().split(",")
                amount = int(amount)
                if action == "supply":
                    supply_total += amount
                elif action == "buy":
                    buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w") as out_file:
        out_file.write("supply,{}\nbuy,{}\nresult,{}\n".format(
            supply_total, buy_total, result))
