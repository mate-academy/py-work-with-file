def create_report(data_file_name: str, report_file_name: str) -> None:
    grouped_data = {"supply": 0, "buy": 0}
    with open(data_file_name) as data_file:
        for line in data_file:
            if line:
                row = line.split(",")
                grouped_data[row[0]] += int(row[1])
    grouped_data["result"] = grouped_data["supply"] - grouped_data["buy"]

    with open(report_file_name, "w") as report_file:
        for key, value in grouped_data.items():
            report_file.write(f"{key},{value}\n")
