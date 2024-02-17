def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as read,
          open(report_file_name, "w") as write):
        lines = read.read().splitlines()

        supply_total = 0
        buy_total = 0

        for line in lines:
            if line.strip():
                operation, amount_str = line.split(",")
                amount = int(amount_str)

                if operation == "supply":
                    supply_total += amount
                elif operation == "buy":
                    buy_total += amount

        result = supply_total - buy_total

        write.write(f"supply,{supply_total}\nbuy,{buy_total}\nresult,{result}\n")
