def create_report(data_file_name: str, report_file_name: str):
    res = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as origin_file:
        for line in origin_file:
            content = line.split(",")
            if content[0] == "buy":
                res["buy"] += int(content[1])
            elif content[0] == "supply":
                res["supply"] += int(content[1])
    res["result"] = int(res["supply"]) - int(res["buy"])
    with open(report_file_name, "w") as report_file:
        for key, value in res.items():
            report_file.write(f"{key},{value}\n")
