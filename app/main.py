def create_report(data_file_name: str, report_file_name: str):
    dict_of_data = {
        "supply": 0,
        "buy": 0
                }

    with open(data_file_name, "r") as dt_file, open(f"{report_file_name}", "w") as file_out:
        for line in dt_file.readlines():
            line = line.split(",")
            dict_of_data[line[0]] += int(line[1].replace("\n", ''))
        dict_of_data["result"] = dict_of_data["supply"] - dict_of_data["buy"]


        for key, value in dict_of_data.items():
            file_out.write(f"{key},{value}\n")
