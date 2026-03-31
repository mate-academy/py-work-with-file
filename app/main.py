def create_report(data_file_name: str, report_file_name: str) -> None:
    res_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as ffile:
        cur_line = ffile.readline()
        while cur_line != "":
            met = cur_line.split(",")
            res_dict[met[0]] += int(met[1].replace("\n", ""))
            cur_line = ffile.readline()
    ffile = open(report_file_name, "w")
    ffile.write(f"supply,{res_dict['supply']}\n")
    ffile.write(f"buy,{res_dict['buy']}\n")
    ffile.write(f"result,{res_dict['supply'] - res_dict['buy']}\n")
    ffile.write("")
    ffile.close()


# create_report("../apples.csv", "1")
# f= open("../apples.csv","r")
# print(f.readlines(1))
