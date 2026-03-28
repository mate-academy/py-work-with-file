def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    with (open(data_file_name) as data_file,
          open(report_file_name, "w") as report_file):
        supply = 0
        buy = 0
        for line in data_file:
            operation_type, amount = line.split(",")
            if operation_type == "supply":
                supply += int(amount)
            if operation_type == "buy":
                buy += int(amount)
        report_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{supply - buy}\n")
