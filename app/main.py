def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    data_file = open(data_file_name, "r")
    for line in data_file:
        name = line.strip().split(",")
        data_dict[name[0]] += int(name[1])

    data_file .close()

    data_dict["result"] = data_dict["supply"] - data_dict["buy"]

    with open(report_file_name, "w") as report_file:
        for key, value in data_dict.items():
            report_file.write(f"{key},{value}")
