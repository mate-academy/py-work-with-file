def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}
    with open(data_file_name) as f1:
        for line in f1:
            report_dict[line.split(",")[0]] += int(line.split(",")[1])
    supply = str(report_dict["supply"])
    buy = str(report_dict["buy"])
    result = str(report_dict["supply"] - report_dict["buy"])
    with open(report_file_name, "a") as f2:
        f2.write("supply" + "," + supply)
        f2.write("\nbuy" + "," + buy)
        f2.write("\nresult" + "," + result + "\n")
