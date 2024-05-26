def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    data = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    with open("../" + data_file_name, "r") as f:
        line = f.readline().strip("\n")
        while line:
            operation, amount = line.split(",")
            data[operation] += int(amount)
            line = f.readline().strip("\n")
        data["result"] = data["supply"] - data["buy"]

    with open(report_file_name, "w") as f:
        for operation, amount in data.items():
            f.write(",".join((operation, str(amount))) + "\n")
