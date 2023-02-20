def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file,\
            open(report_file_name, "w") as report_file:
        supply = 0
        buy = 0
        for data in data_file:
            action, value = data.split(",")
            if action == "supply":
                supply += int(value)
            if action == "buy":
                buy += int(value)
        report_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{supply - buy}\n")
