def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {}
    with open(data_file_name, "r") as file:
        for line in file:
            key, value = line.split(",")
            key = str(key)
            value = int(value)
            report.update({key: report.get(key, 0) + value})
        report.update({"result": report.get("supply") - report.get("buy")})

    with open(report_file_name, "w") as file:
        file.write(f"supply,{report.get('supply')}\n")
        file.write(f"buy,{report.get('buy')}\n")
        file.write(f"result,{report.get('result')}\n")
