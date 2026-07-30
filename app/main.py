def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        report = [line.rstrip("\n").split(",") for line in data_file]

        result = {}
        for item in report:
            if item[0] not in result:
                result[item[0]] = int(item[1])
                continue
            result[item[0]] += int(item[1])

        report_file.write("supply," + f'{result["supply"]}\n')
        report_file.write("buy," + f'{result["buy"]}\n')
        report_file.write("result," + f'{result["supply"] - result["buy"]}\n')
