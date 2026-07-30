def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as in_file, \
            open(report_file_name, "w") as out_file:

        report = {"supply": 0, "buy": 0}
        for line in in_file.readlines():
            if line:
                line_parts = line.split(",")
                report[line_parts[0]] += int(line_parts[1])

        res = ""
        for key in report:
            res += key + "," + str(report[key]) + "\n"

        res += "result," + str(report["supply"] - report["buy"]) + "\n"

        out_file.write(res)
