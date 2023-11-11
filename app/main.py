def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source:
        new_dict = {"supply": 0, "buy": 0}
        for line in source:
            new_dict[line.split(",")[0]] += line.split(",")[1]
        new_dict["result"] = new_dict.get("supply") - new_dict.get("buy")
        with open(report_file_name, "w") as result_file:
            for key, value in new_dict.items():
                result_file.write(f"{key},{value}\n")
