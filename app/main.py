

def create_report(data_file_name: str, report_file_name: str) -> None:

    report_dict = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as csv_file:
        for line in csv_file:

            data = line.split(",")
            op_type = data[0]
            value = int(data[1])
            report_dict[op_type] += value

    report_dict["result"] = report_dict["supply"] - report_dict["buy"]

    with open(report_file_name, "w") as csv_file:
        for key, value in report_dict.items():
            csv_file.write(f"{key},{value}\n")
