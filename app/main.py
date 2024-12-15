def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    file = open(data_file_name, "r")
    for line in file:
        name = line.strip().split(",")
        data_dict[name[0]] += int(name[1])

    file.close()

    data_dict["result"] = data_dict["supply"] - data_dict["buy"]

    with open(report_file_name, "w") as file:
        for key, value in data_dict.items():
            file.write(f"{key},{value}")
