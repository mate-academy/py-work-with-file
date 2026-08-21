def create_report(data_file_name: str, report_file_name: str) -> None:
    message = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as f:
        for line in f:
            if line != "":
                message[line.split(",")[0]] += int(line.split(",")[1])
        message["result"] = message["supply"] - message["buy"]
    with open(report_file_name, "a") as report:
        for key, value in message.items():
            report.write(f"{key},{value}\n")
