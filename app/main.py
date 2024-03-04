def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"supply": 0, "buy": 0, "result": 0}

    with open(data_file_name, "r") as data_file:
        for line in data_file.readlines():
            line = line.replace("\n", "")
            line = line.split(",")
            for key in result.keys():
                if line[0] == key:
                    result[key] += int(line[1])

    result["result"] = result["supply"] - result["buy"]

    with open(report_file_name, "w") as file:
        for key, value in result.items():
            file.write(f"{key},{value}\n")
