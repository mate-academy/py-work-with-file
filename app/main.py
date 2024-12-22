def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)
    raport = {
        "supply": 0,
        "buy": 0
    }

    for line in data_file:
        res = line.split(",")
        if res[0] == "supply":
            raport["supply"] += int(res[1])
        else:
            raport["buy"] += int(res[1])

    new_file = open(report_file_name, "w")
    raport["result"] = raport["supply"] - raport["buy"]
    for key, value in raport.items():
        new_file.write(f"{key},{str(value)}\n")
    new_file.close()
