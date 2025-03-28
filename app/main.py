def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as f:
        for line in f.readlines():
            data[line[0: line.index(",")]] += int(line[line.index(",") + 1:])
    data["result"] = data["supply"] - data["buy"]
    with open(report_file_name, "w") as file:
        for key in data:
            file.write(key + "," + str(data[key]) + "\n")
