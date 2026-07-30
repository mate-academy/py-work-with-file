def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name) as file:
        for line in file:
            parts = line.strip().split(",")
            name = parts[0]
            price = int(parts[1])

            if name == "supply":
                supply += price
            elif name == "buy":
                buy += price
    result = supply - buy
    supply = f"supply,{supply}"
    buy = f"buy,{buy}"
    result = f"result,{result}"

    with open(report_file_name, "w") as report_file:
        report_file.write(supply + "\n")
        report_file.write(buy + "\n")
        report_file.write(result + "\n")
