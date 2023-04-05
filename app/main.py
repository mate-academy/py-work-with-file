def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        data = {}
        for line in data_file:
            operation_type, amount = line.split(",")
            if data.get(operation_type):
                data[operation_type] += int(amount)
            else:
                data[operation_type] = int(amount)
        report_file.write(f"supply,{data.get('supply')}\n"
                          f"buy,{data.get('buy')}\n"
                          f"result,{data.get('supply') - data.get('buy')}\n")
