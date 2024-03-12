def create_report(data_file: str, report_file: str) -> None:
    with (
        open(data_file, "r") as data, open(report_file, "w") as report
    ):
        info = {
            "supply": 0,
            "buy": 0,
            "result": 0
        }
        for line in data.readlines():
            line = line.split(",")
            info[line[0]] += int(line[1])
        info["result"] = info["supply"] - info["buy"]
        for key, value in info.items():
            report.write(key + "," + str(value) + "\n")
