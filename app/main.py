def create_report(data_file_name: str, report_file_name: str) -> None:
    print(data_file_name, report_file_name)
    with (open(data_file_name, "r") as fin,
          open(report_file_name, "w") as fout):
        res_dict = {"supply": 0, "buy": 0}
        while True:
            in_str = fin.readline()
            if in_str == "":
                break
            instr = in_str.split(",")
            res_dict[instr[0]] += int(instr[1])
        outstr = "supply," + f"""{res_dict["supply"]}\nbuy""" + "," + \
                 f"""{res_dict["buy"]}\nresult""" + "," + \
                 f"""{res_dict["supply"] - res_dict["buy"]}\n"""
        print(outstr)
        fout.write(outstr)
