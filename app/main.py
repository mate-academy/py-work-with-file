def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        data = {"supply": 0, "buy": 0}

        for line in data_file:
            key, amount = line.strip().split(",")
            amount = int(amount)
            data[key] += amount

        data["result"] = (data["supply"] - data["buy"])

    with open(report_file_name, "w") as report_file:

        for key, value in data.items():
            report_file.write(f"{key},{value}\n")
