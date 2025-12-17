def create_report(data_file_name: str, report_file_name: str) -> None:
    some_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if line:
                info = line.split(",")
                some_dict[info[0]] += int(info[1])
    result = some_dict["supply"] - some_dict["buy"]
    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(some_dict["supply"]) + "\n")
        report_file.write("buy," + str(some_dict["buy"]) + "\n")
        report_file.write("result," + str(result) + "\n")
