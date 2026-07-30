def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file:
        dict_of_data = {"supply": 0, "buy": 0}
        for line in data_file:
            key = line.strip("\n").split(",")[0]
            value = line.strip("\n").split(",")[1]
            if key == "supply":
                dict_of_data["supply"] += int(value)
            if key == "buy":
                dict_of_data["buy"] += int(value)
        dict_of_data["result"] = dict_of_data["supply"] - dict_of_data["buy"]
    with open(report_file_name, "w") as report_file:
        for key, value in dict_of_data.items():
            report_file.write(f"{key},{value}\n")
