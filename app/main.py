def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "a") as report_file):

        values = [
            line.rstrip().split(",")
            for line in data_file if line.strip()
        ]
        values_dict = {"supply": 0, "buy": 0}

        for operation, amount in values:
            values_dict[operation] += int(amount)

        values_dict["result"] = values_dict["supply"] - values_dict["buy"]

        for operation, amount in values_dict.items():
            report_file.write(f"{operation},{amount}\n")
