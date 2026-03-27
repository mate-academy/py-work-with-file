def create_report(data_file_name: str, report_file_name: str):
    result_dict = dict()
    with open(data_file_name, "r") as file_in:
        for line in file_in:
            if line == "":
                continue
            list_data_line = line.split(",")
            if result_dict.get(list_data_line[0]) is None:
                result_dict[list_data_line[0]] = int(list_data_line[1])
            else:
                result_dict[list_data_line[0]] += int(list_data_line[1])
    list_strings = [f"{key},{result_dict[key]}\n"
                    for key in result_dict.keys()]
    list_strings.sort(reverse=True)
    list_strings.append(f"result,"
                        f"{result_dict['supply'] - result_dict['buy']}\n")
    with open(report_file_name, "w") as file_out:
        file_out.writelines(list_strings)
