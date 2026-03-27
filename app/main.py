from csv import reader


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, "r") as data:
        data_reader = reader(data)
        for row in data_reader:
            action, quantity = row
            quantity = int(quantity)
            if action == "supply":
                supply_total += quantity
            elif action == "buy":
                buy_total += quantity

    result = supply_total - buy_total

    with open(report_file_name, "a") as rep:
        rep.write(f"supply,{supply_total}\n")
        rep.write(f"buy,{buy_total}\n")
        rep.write(f"result,{result}\n")
