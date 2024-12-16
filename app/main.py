def create_report(data_file_name: str, report_file_name: str) -> None:
    calculations = {}

    try:
        source = open(data_file_name)
    except FileNotFoundError as error:
        print(error)
    else:
        for line in source:
            key = line.split(",")[0]
            if key in calculations:
                calculations[key] += int(line.split(",")[1][:-1])
            else:
                calculations[key] = int(line.split(",")[1][:-1])
        source.close()

    report = open(report_file_name, "w")
    if calculations:
        report.write("supply," + f"{calculations["supply"]}\n")
        report.write("buy," + f"{calculations["buy"]}\n")
        report.write(
            "result," + f"{calculations["supply"] - calculations["buy"]}\n"
        )
    report.close()
