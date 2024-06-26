def create_report(data_file_name: str, report_file_name: str) -> None:
    file_ = open(data_file_name, "r")
    lines = file_.readlines()
    result = {"supply": 0, "buy": 0}
    for line in lines:
        if line == "":
            continue
        words = line.split(",")
        key, value = words
        result[key] += int(value)
    file_.close()
    result["result"] = result["supply"] - result["buy"]

    new_file = open(report_file_name, "w")
    for key, value in result.items():
        new_file.write(f"{key},{value}\n")
    new_file.close()
