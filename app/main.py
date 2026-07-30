def create_report(data_file_name: str, report_file_name: str) -> None:
    new_data = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue

            name, value = line.split(",")
            new_data[name] += int(value)

    result = new_data["supply"] - new_data["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{new_data['supply']}\n")
        report_file.write(f"buy,{new_data['buy']}\n")
        report_file.write(f"result,{result}\n")
