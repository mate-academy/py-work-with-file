def create_report(data_file_name: str, report_file_name: str):
    input_file = open(data_file_name, "r")
    report_dict = {
        "supply": 0,
        "buy": 0
    }

    for line in input_file:
        split_line = line.split(",")
        key = split_line[0]
        value = int(split_line[1])
        report_dict[key] += value

    report_dict["result"] = report_dict["supply"] - report_dict["buy"]
    input_file.close()

    output_file = open(report_file_name, "a")
    for key, value in report_dict.items():
        output_file.write(f"{key},{value}\n")
    output_file.close()
