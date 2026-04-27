def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as file:
        for line in file:
            operation, amount = line.strip().split(",")
            amount = int(amount)

            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount
    result = supply_total - buy_total

    with open(report_file_name, "w") as file:
        file.write(f"supply, {supply_total}\n")
        file.write(f"buy, {buy_total}\n")
        file.write(f"result, {result}\n")


create_report("../apples.csv", "../apples_report.csv")
create_report("../bananas.csv", "../bananas_report.csv")
create_report("../grapes.csv", "../grapes_report.csv")
create_report("../oranges.csv", "../oranges_report.csv")
