def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    with open(data_file_name, "r") as file:
        line = file.readline()
        while line:
            operation, amount = line.split(",")
            data[operation] += amount
            line = file.readline().strip()
        data["result"] = data["supply"] - data["buy"]

    with open(report_file_name, "w") as file:
        for operation, amount in data.items:
            file.write(",".join((operation, str(amount))) + "\n")
