def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as f:
        data = f.readlines()
        for i in data:
            split_data = i.split(",")
            data_dict[split_data[0]] += int(split_data[1][:-1])

        data_dict["result"] = data_dict["supply"] - data_dict["buy"]

    with open(report_file_name, "w") as f:

        for key, value in data_dict.items():
            f.write(f"{key},{value}\n")
