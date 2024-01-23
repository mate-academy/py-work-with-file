def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        output = {"supply": 0, "buy": 0}
        for line in data_file:
            operation, amount = line.split(",")
            output[operation] = output.get(operation) + int(amount)

        output["result"] = output.get("supply") - output.get("buy")

    with open(report_file_name, "w") as report_file:
        for key, value in output.items():
            report_file.write(f"{key},{value}\n")
