def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file, \
            open(report_file_name, "w") as report_file:
        report = {"supply": 0, "buy": 0, "result": 0}
        while True:
            line = data_file.readline()
            if line == "":
                break
            temp = line.replace("\n", "").split(",")
            report[temp[0]] += int(temp[1])
        report["result"] = report["supply"] - report["buy"]
        for key in report:
            report_file.write(f"{key},{report[key]}\n")
