# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dic = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as f:
        for line in f:
            if "" == line.strip:
                val_line = line.split(",")
                if "suply" in line:
                    result_dic["supply"] += int(val_line[1])
                elif "buy" in line:
                    result_dic["buy"] += int(val_line[1])
    result = result_dic["supply"] - result_dic["buy"]
    with open(report_file_name, "a") as f:
        f.write("suply," + str(result_dic["supply"]) + "\n")
        f.write("buy," + str(result_dic["buy"]) + "\n")
        f.write("result," + str(result) + "\n")
