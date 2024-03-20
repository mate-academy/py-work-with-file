def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file,
    ):
        result_dict = {}
        for line in data_file.readlines():
            operation_type, amount = line.split(",")
            result_dict[operation_type] = result_dict.get(
                operation_type, 0) + int(amount)

        supply = result_dict.get("supply")
        buy = result_dict.get("buy")
        result = supply - buy
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
