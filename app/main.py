def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    with open(data_file_name, "r") as data:
        for line in data.readlines():
            tokens = line.split(",")

            if len(tokens) != 2:
                continue

            result_dict[tokens[0]] += int(tokens[1])

    result_dict["result"] = result_dict["supply"] - result_dict["buy"]

    with open(report_file_name, "w") as report:
        for key, value in result_dict.items():
            report.write(f"{key},{value}\n")
