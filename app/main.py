def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data:
        supply = 0
        buy = 0
        for line in data:
            if line.strip():
                split_line = line.split(",")
                operation = split_line[0]
                amount = int(split_line[1])
                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount
        result = supply - buy
    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
