def create_report(data_file_name: str, report_file_name: str) -> None:
    temp_dict = {"supply": 0,
                 "buy": 0,
                 "result": 0,
                 }

    with open(data_file_name, "r") as f:
        for line in f:
            line_lst = line.split(",")
            if line_lst[0] == "supply":
                temp_dict["supply"] += int(line_lst[1])

            if line_lst[0] == "buy":
                temp_dict["buy"] += int(line_lst[1])

        temp_dict["result"] = temp_dict["supply"] - temp_dict["buy"]

    with open(report_file_name, "a") as f:
        f.write(f"supply,{temp_dict['supply']}\n"
                f"buy,{temp_dict['buy']}\n"
                f"result,{temp_dict['result']}\n")
