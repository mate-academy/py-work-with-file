def create_report(data_file_name: str, report_file_name: str) -> None:
    data_combined = {
        "supply": 0,
        "buy": 0,
    }

    with open(data_file_name, "r") as source_file:
        for line in source_file.readlines():
            line = line[:-1]
            if line.split(",")[0] in data_combined:
                data_combined[line.split(",")[0]] += int(line.split(",")[1])

    data_combined["result"] = data_combined["supply"] - data_combined["buy"]

    with open(report_file_name, "w") as destination_file:
        for key, value in data_combined.items():
            destination_file.write(f"{key},{value}\n")
