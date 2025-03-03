def create_report(data_file: str, report_file_name: str) -> None:
    with open(data_file, "r") as file:
        data_list = file.readlines()
        new_list = []
        new_dict = {}

        for line in data_list:
            new_list.append(line.strip("\n").split(","))

        for item in new_list:
            if item[0] not in new_dict:
                new_dict[item[0]] = int(item[1])
            else:
                new_dict[item[0]] += int(item[1])

    with open(report_file_name, "w") as f:
        f.write(f"supply,{new_dict["supply"]}\n")
        f.write(f"buy,{new_dict["buy"]}\n")
        f.write(f"result,{new_dict["supply"] - new_dict["buy"]}\n")
