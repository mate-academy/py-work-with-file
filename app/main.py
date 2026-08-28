def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file:
        total = {}
        for string in data_file:
            string = string.strip("\n")
            operation, amount = string.split(",")
            total[operation] = total.get(operation, 0) + int(amount)

        balance = total["supply"] - total["buy"]
        with open(report_file_name, "w") as report_file:
            for instance, amount in total.items():
                report_file.write(f"{instance},{amount}\n")
            report_file.write(f"result,{balance}\n")
