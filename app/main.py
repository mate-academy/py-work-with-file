def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        new_date = {"supply": 0, "buy": 0, "result": 0}
        for lines in data_file:
            date, amount = lines.split(",")
            new_date[date] += int(amount)
        new_date["result"] = new_date["supply"] - new_date["buy"]
    with open(report_file_name, "a") as report_file:
        for keys, values in new_date.items():
            report_file.write(f"{keys},{values}\n")
