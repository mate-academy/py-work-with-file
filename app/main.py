def create_report(data_file_name: str, report_file_name: str) -> None:
    data_to_write = {"supply": 0, "buy": 0, "result": 0}

    data_file = open(data_file_name, "r")
    for line in data_file:
        data = line.split(",")
        data_to_write[data[0]] += int(data[1])
    data_file.close()

    data_to_write["result"] = data_to_write["supply"] - data_to_write["buy"]

    report_file = open(report_file_name, "w")
    for key, value in data_to_write.items():
        report_file.write(f"{key},{value}\n")
    report_file.close()
