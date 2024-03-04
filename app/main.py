def create_report(data_file_name: str, report_file_name: str):
    dict_check = {}
    with open(data_file_name, "r") as read:
        for line in read:
            new_line = line.replace("\n", "")
            new_line = new_line.split(",")
            if new_line[0] not in dict_check.keys():
                dict_check[new_line[0]] = int(new_line[1])
            else:
                dict_check[new_line[0]] += int(new_line[1])
    with open(report_file_name, "w") as write_rep:
        write_rep.write(f"supply,{dict_check['supply']}\n"
                        f"buy,{dict_check['buy']}\n"
                        f"result,{dict_check['supply']-dict_check['buy']}\n")
