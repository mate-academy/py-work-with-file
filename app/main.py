def create_report(data_file: str, report_file: str) -> None:
    result = {
        "supply": 0,
        "buy": 0
    }
    with open(data_file, "r") as data_from_file:

        while True:
            file_line = data_from_file.readline()

            if not file_line:
                break

            data_type, data = file_line.split(",")
            result[data_type] += int(data)

    result["result"] = result["supply"] - result["buy"]

    with open(report_file, "w") as report:
        for key, value in result.items():
            report.write(key + "," + str(value) + "\n")
