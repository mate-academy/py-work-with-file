def create_report(data_file_name: str, report_file_name: str) -> None:
    report = open(report_file_name, "w")
    data = open(data_file_name, "r")
    new_dict = {}
    for line in data:
        if not line:
            break
        string = line.split(",")
        if new_dict.get(string[0]) is None:
            new_dict[string[0]] = int(string[1])
            continue
        new_dict[string[0]] += int(string[1])
    data.close()
    new_dict["result"] = new_dict["supply"] - new_dict["buy"]
    order = ["supply", "buy", "result"]
    for key in order:
        report.write(key + "," + str(new_dict[key]) + "\n")
    report.close()
