def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {}
    with open(data_file_name, "r") as file:
        for line in file:
            transaction, amount = line.split(",")
            amount = int(amount)
            if transaction not in report:
                report[transaction] = amount
            else:
                report[transaction] += amount
        report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as final:
        final.write("supply," + str(report["supply"]) + "\n")
        final.write("buy," + str(report["buy"]) + "\n")
        final.write("result," + str(report["result"]) + "\n")
