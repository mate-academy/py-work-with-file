import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, encoding="utf-8") as file:
        data = list(csv.reader(file, delimiter=",", quotechar='\"'))
        total = {}
        for operation, amount in data:
            total[operation] = total.get(operation, 0) + int(amount)
        total["result"] = total["supply"] - total["buy"]

    with open(report_file_name, "w") as report:
        report.write(f"supply,{total['supply']}\n")
        report.write(f"buy,{total['buy']}\n")
        report.write(f"result,{total['result']}\n")
