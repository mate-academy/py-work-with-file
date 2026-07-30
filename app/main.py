class Report:
    pass


def create_report(data_file_name: str, report_file_name: str) -> Report :
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file.readlines():
            operation, amount = line.split(",")
            amount = int(amount)
            if operation == "buy":
                buy_total += amount
            elif operation == "supply":
                supply_total += amount
        data_file.close()
    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(supply_total) + "\n")
        report_file.write("buy," + str(buy_total) + "\n")
        report_file.write("result," + str(result) + "\n")
        report_file.close()


if __name__ == "__main__":
    create_report("apples.csv", "report.txt")
