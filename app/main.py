def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name, "r") as data_file:
        for line in data_file.readlines():
            line = line.rstrip("\n").split(",")
            data[line[0]] += int(line[1])

    data["result"] = data["supply"] - data["buy"]

    with open(report_file_name, "w") as report_file:
        for key, value in data.items():
            report_file.write(f"{key},{value}\n")
