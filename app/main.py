def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    my_file = open(data_file_name)
    my_dict = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    for line in my_file:
        split_line = line.split(",")
        my_dict[split_line[0]] += int(split_line[-1])
    my_dict["result"] = my_dict["supply"] - my_dict["buy"]
    my_file.close()
    report_file = open(report_file_name, "w")
    for key, value in my_dict.items():
        report_file.write(f"{key},{value}\n")
    report_file.close()
