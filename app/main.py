def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {"supply": 0, "buy": 0}
    with (
        open(data_file_name, "r") as source,
        open(report_file_name, "w") as report
    ):
        for line in source:
            line = line.split(",")
            if line[0] in data_dict:
                data_dict[line[0]] += int(line[1])
        data_dict["result"] = data_dict["supply"] - data_dict["buy"]
        for key, value in data_dict.items():
            report.write(f"{key},{value}\n")
