def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as f:
        for line in f:
            item = (line.strip().split(","))
            key = item[0]
            value = int(item[1])
            result_dict[key] += value
        result_dict["result"] = result_dict["supply"] - result_dict["buy"]
    with open(report_file_name, "w") as f:
        for key, value in result_dict.items():
            f.write(f"{key},{value}\n")
