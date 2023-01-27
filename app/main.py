def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        supply = 0
        buy = 0
        for line in data_file:
            operation_type, amount = line.split(",")
            print(line, operation_type, amount)
            if operation_type == "supply":
                supply += int(amount)
            if operation_type == "buy":
                buy += int(amount)
        report_file.write(f"result,{supply - buy}")
