def create_report(data_file_name: str, report_file_name: str) -> None:

    result_dic = {"supply":0, "buy":0}
    with open(data_file_name, "r",) as file:
        for line in file:
            if "," in line.strip():
                vales_line = line.split(",")
                if "supply" in line:
                    result_dic["supply"] += int(vales_line[1])
                elif "buy" in line:
                    result_dic["buy"] += int(vales_line[1])
    result = result_dic["supply"] - result_dic["buy"]
    with open(report_file_name, "a") as file:
        file.write("supply," + str(result_dic["supply"]) + "\n")
        file.write("buy," + str(result_dic["buy"]) + "\n")
        file.write("result," + str(result) + "\n")
