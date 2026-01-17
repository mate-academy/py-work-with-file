def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:

        data_list = [item.split(",") for item in data_file.readlines()]
        data_dict = {"supply": 0, "buy": 0}
        for line in data_list:
            if line[0] == "supply":
                data_dict["supply"] += int(line[1].rstrip())
            if line[0] == "buy":
                data_dict["buy"] += int(line[1].rstrip())
        data_dict["result"] = data_dict["supply"] - data_dict["buy"]

    with open(report_file_name, "w") as report_file:
        for key, value in data_dict.items():
            report_file.write("%s\n" % f"{key},{value}")
