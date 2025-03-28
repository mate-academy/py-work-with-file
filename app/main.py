def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as date_file,
          open(report_file_name, "w") as report_file):
        report = [line.rstrip("\n").split(",") for line in date_file]

        result = {}
        for element in report:
            if element[0] not in result:
                result[element[0]] = int(element[1])
            else:
                result[element[0]] += int(element[1])

        report_file.write("supply," + f'{result["supply"]}\n')
        report_file.write("buy," + f'{result["buy"]}\n')
        report_file.write("result," + f'{result["supply"] - result["buy"]}\n')
