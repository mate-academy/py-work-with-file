def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {}

    with open(data_file_name, "r") as file:
        for line in file:
            current_line = line.rstrip().split(",")

            if len(current_line) >= 2 and current_line[0].strip():
                if current_line[0] in report:
                    report[current_line[0]] += int(current_line[1])
                else:
                    report[current_line[0]] = int(current_line[1])

    with open(report_file_name, "w") as new_file:
        result = report.get("supply", 0) - report.get("buy", 0)

        new_file.write(f'supply,{report.get("supply", 0)}\n')
        new_file.write(f'buy,{report.get("buy", 0)}\n')
        new_file.write(f'result,{result}\n')
