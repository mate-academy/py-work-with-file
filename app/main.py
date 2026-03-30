def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = {"supply": 0, "buy": 0}
    with open(data_file_name) as data_file:
        for line in data_file:
            key, value = line[:len(line) - 1].split(",")
            supply[key] += int(value)

    with open(report_file_name, "a") as report_file:
        supply["result"] = supply["supply"] - supply["buy"]
        for key, value in supply.items():
            report_file.write(f"{key},{value}\n")
