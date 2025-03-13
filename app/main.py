def create_report(data_file: str, report_file: str):
    with open(f"{data_file}", "r") as r, open(f"{report_file}", "w") as w:
        new_dict = {"supply": 0, "buy": 0}
        read_line = r.readline()
        while read_line != "":
            r_list = read_line.strip().split(",")
            new_dict[r_list[0]] += int(r_list[1])
            read_line = r.readline()
        w.write(f"supply,{new_dict['supply']}\n"
                f"buy,{new_dict['buy']}\n"
                f"result,{new_dict['supply'] - new_dict['buy']}\n"
                )
