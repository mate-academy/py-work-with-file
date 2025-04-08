def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    file = open(data_file_name.csv, "r")

    for line in file:
        if line.strip():
            parts = line.strip().split(",")
            operation = parts[0]
            amount = int(parts[1])

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    file.close()

    report = open(report_file_name, "w")
    report.write(f"supply,{supply}\n")
    report.write(f"buy,{buy}\n")
    report.write(f"result,{supply - buy}\n")
    report.close()
