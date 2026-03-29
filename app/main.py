def create_report(data_file_name: str, report_file_name: str) -> None:
    res = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            row = line.split(",")
            if row[0] == "supply":
                res["supply"] += int(row[1])
            else:
                res["buy"] += int(row[1])

    res["result"] = res["supply"] - res["buy"]

    with open(report_file_name, "w") as report_file:
        for key, value in res.items():
            report_file.write(f"{key},{value}\n")
