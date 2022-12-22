def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(f"{data_file_name}", "r") as source:
        with open(f"{report_file_name}", "a") as receiver:
            supply, buy = 0, 0
            for line in source:
                operation, amount = line.split(",")
                amount = int(amount[:-1])
                if operation == "supply":
                    supply += amount
                if operation == "buy":
                    buy += amount
            receiver.write(f"supply,{supply}\n")
            receiver.write(f"buy,{buy}\n")
            receiver.write(f"result,{supply - buy}\n")
