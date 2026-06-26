def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for line in data_file.readlines():
            clean_line = line.strip()
            if clean_line:
                data[clean_line.split(",")[0]] += int(clean_line.split(",")[1])

    data["result"] = data["supply"] - data["buy"]
    print(data)

    with open(report_file_name, "w") as report_file:
        for key, value in data.items():
            report_file.write(f"{key},{value}\n")
