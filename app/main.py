def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_value = 0
    supply_value = 0
    with open(data_file_name, "r") as source:
        for line in source.readlines():
            data_type, value = line.split(",")
            if data_type == "buy":
                buy_value += int(value)
            else:
                supply_value += int(value)
    with open(report_file_name, "w") as output:
        output.write(f"supply,{supply_value}\n")
        output.write(f"buy,{buy_value}\n")
        output.write(f"result,{supply_value - buy_value}\n")
