import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as file:
        data = csv.reader(file)
        total = {"supply": 0, "buy": 0}

        for transaction, amount in data:
            total[transaction] = total.get(transaction, 0) + int(amount)

        total["result"] = total["supply"] - total["buy"]

    with open(report_file_name, "w") as file:
        data = csv.writer(file)

        for transaction, amount in total.items():
            data.writerow([transaction, amount])
