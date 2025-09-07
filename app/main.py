def create_report(data_file_name: str, report_file_name: str) -> None:

    data_file = open(data_file_name, "r")
    report_file = open(report_file_name, "w")

    lines = data_file.readlines()

    print(lines)

    report_object = {
        "supply": 0,
        "buy": 0,
        "result": 0,
    }

    for line in lines:
        words = line.split(",")

        if words[0] in report_object:
            report_object[words[0]] += int(words[1])

    report_object["result"] = report_object["supply"] - report_object["buy"]

    for key, value in report_object.items():
        report_string = key + "," + str(value) + "\n"
        report_file.write(report_string)

    data_file.close()
    report_file.close()

# create_report("../apples.csv", "apples_report.csv")
