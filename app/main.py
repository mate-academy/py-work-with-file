
def create_report(data_file_name: str, report_file_name: str) -> any:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as file:
        reader = file.readlines()
        for row in reader:
            x_row = row.split(",")
            operation = x_row[0]
            amount = int(x_row[1])
            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "a") as file:
        file.writelines(",".join(["supply", str(supply_total)]) + "\n")
        file.writelines(",".join(["buy", str(buy_total)]) + "\n")
        file.writelines(",".join(["result", str(result)]) + "\n")
