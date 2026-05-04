def create_report(data_file_name: str, report_file_name: str) -> None:
    if data_file_name and report_file_name:
        res_dict = {}
        with open(data_file_name, "r") as data_file:
            data = data_file.read()
            for line in data.split("\n"):
                if line != "":
                    temp_list = line.split(",")
                    if temp_list[0] not in res_dict:
                        res_dict[temp_list[0]] = int(temp_list[1])
                    else:
                        res_dict[temp_list[0]] += int(temp_list[1])
        res = ""
        supply_total = res_dict.get("supply", 0)
        buy_total = res_dict.get("buy", 0)
        result_total = supply_total - buy_total
        res += f"supply,{supply_total}\n"
        res += f"buy,{buy_total}\n"
        res += f"result,{result_total}\n"
        with open(report_file_name, "w") as report_file:
            report_file.write(res)
