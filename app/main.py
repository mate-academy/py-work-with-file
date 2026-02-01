def create_report(data_file_name: str, report_file_name: str) -> None:
    data_split = {"supply": 0, "buy": 0, "result": 0}

    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        for line in file_in:
            operation, amount = line.split(",")
            amount = int(amount)
            if operation in data_split:
                data_split[operation] += amount
            else:
                data_split[operation] = amount
        data_split["result"] = data_split["supply"] - data_split["buy"]
        file_out.write(
            "supply," + str(data_split["supply"]) + "\n"
            + "buy," + str(data_split["buy"]) + "\n"
            + "result," + str(data_split["result"]) + "\n"
        )
