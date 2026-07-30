def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        data_dict = {"supply": 0, "buy": 0}
        for line in data_file.readlines():
            operation, amount = line.split(",")
            data_dict[operation] += int(amount)
        report_file.write(f"supply,{data_dict['supply']}\n")
        report_file.write(f"buy,{data_dict['buy']}\n")
        report_file.write(f"result,{data_dict['supply'] - data_dict['buy']}\n")
