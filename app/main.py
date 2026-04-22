def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        data = data_file.read()

    report_dict = {}
    for line in data.splitlines():
        key, value = line.split(",")
        if key.strip() in report_dict:
            report_dict[key.strip()] += int(value.strip())
        else:
            report_dict[key.strip()] = int(value.strip())

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{report_dict.get('supply', 0)}\n")
        report_file.write(f"buy,{report_dict.get('buy', 0)}\n")
        result_val = report_dict.get("supply", 0) - report_dict.get("buy", 0)
        report_file.write(f"result,{result_val}\n")
