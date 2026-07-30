def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_value = {}
    if ".csv" in data_file_name:
        with open(data_file_name, "r") as source, \
                open(report_file_name, "w") as report:
            dates_of_file = source.read().splitlines()
            for date in dates_of_file:
                key, value = date.split(",")
                if key in dict_value.keys():
                    dict_value[key] += int(value)
                else:
                    dict_value[key] = int(value)
            dict_value["result"] = dict_value["supply"] - dict_value["buy"]

            report.write("supply," + str(dict_value["supply"]) + "\n"
                         "buy," + str(dict_value["buy"]) + "\n"
                         "result," + str(dict_value["result"]) + "\n")
