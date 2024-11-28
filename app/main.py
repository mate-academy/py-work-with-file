def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name) as f:
        for line in f:
            values = line.split(",")
            if values[0] == "supply":
                supply += int(values[1])
            elif values[0] == "buy":
                buy += int(values[1])

    result = supply - buy

    with open(report_file_name, "a") as r:
        r.write(f"supply,{supply}\n")
        r.write(f"buy,{buy}\n")
        r.write(f"result,{result}\n")
