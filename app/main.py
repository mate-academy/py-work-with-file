def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    market_data = dict()

    for line in data_file:
        name = line[:line.find(",")]
        value = line[line.find(",") + 1:]
        if not market_data.get(name):
            market_data[name] = int(value)
        else:
            market_data[name] += int(value)

    data_file.close()
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{market_data['supply']}\n")
    report_file.write(f"buy,{market_data['buy']}\n")
    result = market_data["supply"] - market_data["buy"]
    report_file.write(f"result,{result}\n")
    report_file.close()
