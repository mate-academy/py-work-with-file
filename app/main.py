def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with (
        open(data_file_name, "r") as read_file,
        open(report_file_name, "a") as report
    ):
        temp = {"supply": 0, "buy": 0}
        for line in read_file.readlines():
            content = line.split(",")
            temp[content[0]] = temp[content[0]] + int(content[1])
        result = temp["supply"] - temp["buy"]
        for key, value in temp.items():
            report.write(key + "," + str(value) + "\n")
        report.write("result" + "," + str(result) + "\n")
