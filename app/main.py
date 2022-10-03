def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(f"{data_file_name}") as data_in:
        data = {}
        for line in data_in:
            if data.get(line.split(",")[0]):
                data[line.split(",")[0]] += int(line.split(",")[1])
            else:
                data[line.split(",")[0]] = int(line.split(",")[1])

    with open(f"{report_file_name}", "w") as report:
        report.write(f"supply,{data['supply']}\n"
                     f"buy,{data['buy']}\n"
                     f"result,{data['supply'] - data['buy']}\n")
