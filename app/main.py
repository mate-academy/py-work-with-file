def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    supply_value = 0
    buy_value = 0

    with open(data_file_name, "r") as file_in:
        for line in file_in.readlines():
            action, value = line.split(",")
            if action == "supply":
                supply_value += int(value)
            if action == "buy":
                buy_value += int(value)
        result = supply_value - buy_value

    with open(report_file_name, "w") as file_out:
        file_out.write(f"supply,{supply_value}\n")
        file_out.write(f"buy,{buy_value}\n")
        file_out.write(f"result,{result}\n")
