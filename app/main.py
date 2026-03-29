def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as f:
        while True:
            line = f.readline()
            if line == "":
                break
            line = line.strip().split(",")
            result[line[0]] += int(line[1])
    result["result"] = result.get("supply") - result.get("buy")
    with open(report_file_name, "w") as f:
        for key, value in result.items():
            f.write(key + "," + str(value) + "\n")
