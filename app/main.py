def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}
    file1 = open(data_file_name)
    for line in file1.readlines():
        data[line[0: line.index(",")]] += int(line[line.index(",") + 1:])
    data["result"] = data["supply"] - data["buy"]
    file2 = open(report_file_name, "w")
    for key in data:
        file2.write(key + "," + str(data[key]) + "\n")
