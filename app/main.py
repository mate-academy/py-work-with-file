def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as input_file:
        parsed_data = {}
        for line in input_file.readlines():
            line = line.replace("\n", "").split(",")
            if line[0] not in parsed_data.keys():
                parsed_data[line[0]] = int(line[1])
                continue
            parsed_data[line[0]] += int(line[1])

        try:
            parsed_data["result"] = parsed_data["supply"] - parsed_data["buy"]
            with open(report_file_name, "w") as report_file:
                report_file.write(
                    "supply," + str(parsed_data["supply"]) + "\n"
                )
                report_file.write(
                    "buy," + str(parsed_data["buy"]) + "\n"
                )
                report_file.write(
                    "result," + str(parsed_data["result"]) + "\n"
                )
        except KeyError(
                "There no enough data in data file. "
                "Report file was not created."
        ):
            pass
