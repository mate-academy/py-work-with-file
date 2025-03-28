def create_report(data_file: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0}

    with open(data_file, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            position = line.split(",")
            if position[0] in report:
                report[position[0]] += int(position[1])
            else:
                report[position[0]] = int(position[1])

    with open(report_file_name, "w") as file:
        file.write(f'supply,{report["supply"]}\n')
        file.write(f'buy,{report["buy"]}\n')
        result = report["supply"] - report["buy"]
        file.write(f"result,{result}\n")


create_report("apples.csv", "apples_report.csv")
