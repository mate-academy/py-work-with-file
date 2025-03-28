def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file_obj:
        data_ls = [line.strip().split(",") for line in data_file_obj]

    report_dict = {"supply": 0, "buy": 0, "result": 0}
    for row in data_ls:
        if len(row) != 0:
            key = row[0]
            value = int(row[1])
            if key not in report_dict:
                report_dict[key] = value
            else:
                report_dict[key] += value

    report_dict.update({"result": report_dict["supply"] - report_dict["buy"]})

    report_ls = [f"{key},{value}" for key, value in report_dict.items()]

    with open(report_file_name, "w") as report_file_obj:
        report_file_obj.write("\n".join(report_ls) + "\n")
