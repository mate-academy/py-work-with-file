def create_report(data_file_name: str, report_file_name: str):
    with open(f"{data_file_name}", "r") as r, \
            open(f"{report_file_name}", "w") as w:
        my_dict = {"supply": 0, "buy": 0}
        read_line = r.readline()
        while read_line != "":
            r_list = read_line.strip().split(",")
            my_dict[r_list[0]] += int(r_list[1])
            read_line = r.readline()
        w.write(f"supply,{my_dict['supply']}\n"
                f"buy,{my_dict['buy']}\n"
                f"result,{my_dict['supply'] - my_dict['buy']}\n"
                )
