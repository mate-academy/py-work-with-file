def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "a") as file_out):
        data = {"supply": 0, "buy": 0, "result": 0}

        for line in file_in:
            operation, amount = line.split(",")
            data[operation] += int(amount)

        data["result"] = data["supply"] - data["buy"]

        for operation, amount in data.items():
            file_out.write(f"{operation},{amount}\n")
