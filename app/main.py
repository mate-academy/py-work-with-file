def create_report(data_file_name: str, report_file_name: str) -> None:
    read_file = open(data_file_name)
    report_dict = {"supply": 0, "buy": 0, "result": 0}
    for file_line in read_file:
        line = file_line.split(",")
        report_dict[line[0]] += int(line[1].replace("\n", ""))
    report_dict["result"] = report_dict["supply"] - report_dict["buy"]
    read_file.close()
    write_file = open(report_file_name, "w")
    for key, value in report_dict.items():
        write_file.write(f"{key},{value}\n")
    write_file.close()
