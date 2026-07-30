def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    storage = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    for line in data_file:
        if not len(line):
            break
        formatted_str = line.strip().split(",")
        storage[formatted_str[0]] += int(formatted_str[1])

    data_file.close()
    storage["result"] = storage["supply"] - storage["buy"]
    report_file = open(report_file_name, "w")

    for key, value in storage.items():
        report_file.write(f"{key},{value}\n")

    report_file.close()
