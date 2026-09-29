def create_report(data_file_name: str, report_file_name: str) -> None:
    trades = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    data_file = open(data_file_name)
    for line in data_file.readlines():
        trade = line.split(",")
        trades[trade[0]] += int(trade[1])
    data_file.close()

    trades["result"] = trades["supply"] - trades["buy"]

    data_file = open(report_file_name, "w")
    for key, value in trades.items():
        data_file.write(f"{key},{value}\n")
    data_file.close()
