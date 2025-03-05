def create_report(data_file_name: str, report_file_name: str):
    result_dict = {}

    with open(data_file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            split_line = line.split(",")
            if split_line[0] == "supply":
                result_dict[split_line[0]] = \
                    result_dict.get(split_line[0], 0) + int(split_line[1])
            else:
                result_dict[split_line[0]] = \
                    result_dict.get(split_line[0], 0) + int(split_line[1])

        result_dict["result"] = result_dict["supply"] - result_dict["buy"]

    with open(report_file_name, "w") as file:
        file.write(f'supply,{result_dict["supply"]}\n'
                   f'buy,{result_dict["buy"]}\n'
                   f'result,{result_dict["result"]}\n')
