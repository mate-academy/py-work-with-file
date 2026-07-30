def create_report(data_file_name: str, report_file_name: str) -> None:
    input_file = open(data_file_name)

    dictionary = {}
    for line in input_file:
        line = line.strip()
        if not line:
            continue

        key, value = line.split(",")
        value = int(value)
        dictionary[key] = dictionary.get(key, 0) + value

    with open(report_file_name, "w", newline="") as report:
        supply_total = dictionary.get("supply", 0)
        buy_total = dictionary.get("buy", 0)
        result = supply_total - buy_total

        report.write(f"supply,{supply_total}\n")
        report.write(f"buy,{buy_total}\n")
        report.write(f"result,{result}\n")
