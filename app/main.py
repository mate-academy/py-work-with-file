def create_report(data_file_name: str, report_file_name: str) -> None:
    res_dict = {}
    with open(data_file_name) as file:
        for line in file:
            split_line = line.split(",")
            if split_line[0] not in res_dict:
                res_dict[split_line[0]] = int(split_line[1])
            else:
                res_dict[split_line[0]] += int(
                    split_line[1].removesuffix("\n")
                )

        res_dict["result"] = res_dict["supply"] - res_dict["buy"]
        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{res_dict['supply']}\n")
            report_file.write(f"buy,{res_dict['buy']}\n")
            report_file.write(f"result,{res_dict['result']}\n")
