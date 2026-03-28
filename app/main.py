def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(f"{data_file_name}", "r") as origin:
        for transaction in origin.readlines():
            if transaction:
                action, amount = transaction.split(",")
                amount = int(amount)

                if action == "supply":
                    total_supply += amount
                elif action == "buy":
                    total_buy += amount

    result = total_supply - total_buy

    with open(f"{report_file_name}", "w") as report:
        report.write(f"supply,{total_supply}"
                     f"\nbuy,{total_buy}"
                     f"\nresult,{result}\n")
