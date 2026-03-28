def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}

    with open(data_file_name) as data_file:
        for line in data_file:
            line = line.strip()

            key, value = line.split(",")
            value = int(value)

            if key in data:
                data[key] += value

    data["result"] = data["supply"] - data["buy"]

    with open(report_file_name, "w") as report:
        for key in ["supply", "buy", "result"]:
            report.write(f"{key},{data[key]}\n")
