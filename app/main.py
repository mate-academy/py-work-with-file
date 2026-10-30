def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with (
        open(data_file_name) as data_file,
        open(report_file_name, "w") as report_file,
    ):
        for line in data_file:
            operation_type, amount = line.strip().split(",")
            if operation_type == "supply":
                supply += int(amount)
            else:
                buy += int(amount)
        report_file.write(
            f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
        )
