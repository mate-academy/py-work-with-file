def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {}
    with open(data_file_name, "r") as file:
        for line in file:
            key, value = line.split(",")[0], line.split(",")[1]
            if key not in data_dict:
                data_dict[key] = int(value)
            else:
                data_dict[key] += int(value)

    data_dict["result"] = data_dict["supply"] - data_dict["buy"]
    data_list = [f"{key},{value}" for key, value
                 in sorted(data_dict.items(),
                           key=lambda item: item[1],
                           reverse=True)]

    with open(report_file_name, "w") as file:
        file.write("\n".join(data_list) + "\n")
