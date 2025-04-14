def create_report(data_file_name: str, report_file_name: str) -> None:
    tempr_dict = {}

    with open("../" + data_file_name, "r") as file_r:

        for line in file_r:
            line_ls = line.strip().split(",")

            if line_ls[0] in tempr_dict:
                tempr_dict[line_ls[0]] += int(line_ls[1])
            else:
                tempr_dict[line_ls[0]] = int(line_ls[1])

    tempr_dict["result"] = tempr_dict["supply"] - tempr_dict["buy"]

    with open(report_file_name, "w") as file_w:
        file_w.write(f"supply,{tempr_dict['supply']}\n")
        file_w.write(f"buy,{tempr_dict['buy']}\n")
        file_w.write(f"result,{tempr_dict['result']}\n")
