def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as sales:
        calculations = {}

        for line in sales.readlines():
            if not line.strip():
                continue

            key = line.rstrip('\n').split(",")[0]
            value = int(line.rstrip('\n').split(",")[1])

            if key in calculations:
                calculations[key] += value
            else:
                calculations.update({key: value})

    with open(report_file_name, "w") as report:
        supply = calculations['supply']
        buy = calculations['buy']

        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{supply - buy}\n")
