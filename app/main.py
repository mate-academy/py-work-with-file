def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    report_data = {}
    with open(f"../{data_file_name}", "r") as f:
        for line in f:
            data = line.strip().split(",")
            key, value = data[0], int(data[1])
            report_data[key] = report_data.get(key, 0) + value
    result = report_data["supply"] - report_data["buy"]

    with open(report_file_name, "w") as f:
        f.write(f'supply,{report_data["supply"]}\n')
        f.write(f'buy,{report_data["buy"]}\n')
        f.write(f"result,{result}\n")
