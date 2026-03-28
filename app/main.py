def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name) as d:
        for line in d:
            operation, value = line.split(",")
            value = int(value)
            if operation == "supply":
                supply += value
            elif operation == "buy":
                buy += value
    result = supply - buy
    with open(report_file_name, "w") as r:
        r.write(f"supply,{supply}\n")
        r.write(f"buy,{buy}\n")
        r.write(f"result,{result}\n")
