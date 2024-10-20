def create_report(data_file_name: str, report_file_name: str) -> None:
    data_report = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name) as file_to_read:
        for line in file_to_read:
            transaction_amount = line.split(",")
            data_report[transaction_amount[0]] += int(transaction_amount[1])

    data_report["result"] = data_report["supply"] - data_report["buy"]

    with open(report_file_name, "w") as file_to_write:
        for key, value in data_report.items():
            file_to_write.write(f"{key},{value}\n")
