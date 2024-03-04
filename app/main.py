def create_report(data_file_name: str, report_file_name: str):
    data = {}

    with open(data_file_name, "r") as f:
        for line in f:
            operation, amount = line.split(",")

            if operation not in data:
                data[operation] = int(amount)
            else:
                data[operation] += int(amount)

    data["result"] = data["supply"] - data["buy"]

    with open(report_file_name, "w") as f:
        f.write(f"supply,{data['supply']}\n"
                f"buy,{data['buy']}\n"
                f"result,{data['result']}\n")
