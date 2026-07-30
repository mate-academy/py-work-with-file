def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in,\
            open(report_file_name, "w") as file_out:
        total = {}
        for line in file_in:
            if len(line) > 0:
                split_line = line.rstrip().split(",")
                if split_line[0] not in total:
                    total[split_line[0]] = split_line[1]
                else:
                    total[split_line[0]] =\
                        int(total[split_line[0]]) + int(split_line[1])
        total["result"] = int(total["supply"]) - int(total["buy"])
        file_out.write(f"supply,{total['supply']}\n"
                       f"buy,{total['buy']}\n"
                       f"result,{total['result']}\n"
                       )
