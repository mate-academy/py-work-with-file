def create_report(data_file_name: str, report_file_name: str) -> None:
    market_data = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            key, value = line.strip().split(",")
            market_data[key] = market_data.get(key, 0) + int(value)
    market_data["result"] = market_data["supply"] - market_data["buy"]
    with open(report_file_name, "w") as report_file:
        for key, value in market_data.items():
            report_file.write(f"{key},{value}\n")
