def create_report(data_file_name: str, report_file_name: str) -> None:
    buy, supply = 0, 0
    with (open(data_file_name, "r") as source_file,
          open(report_file_name, "w") as report_file):
        for data in source_file:
            op_data, value = data.split(",")
            if op_data == "buy":
                buy += int(value)
            if op_data == "supply":
                supply += int(value)
        report_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{supply - buy}\n")
