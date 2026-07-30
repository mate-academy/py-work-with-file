def create_report(data_file: str, report_file_name: str) -> None:
    with open(data_file, "r") as read_file:
        result = {"supply": 0, "buy": 0}
        for item in read_file:
            key, value = item.strip().split(",")
            result[key] += int(value)
        result["result"] = result["supply"] - result["buy"]
        with open(report_file_name, "w") as write_file:
            for keys, values in result.items():
                write_file.write(f"{keys},{values}\n")
