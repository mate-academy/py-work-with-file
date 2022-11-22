def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in,\
            open(report_file_name, "w") as file_out:
        dict_of_value = {"supply": 0, "buy": 0}

        for line in file_in:
            splitted_line = line.split(",")
            dict_of_value[splitted_line[0]] += int(splitted_line[1])

        for key, value in dict_of_value.items():
            result_string = f"{key},{value}\n"
            file_out.write(result_string)

        result = dict_of_value["supply"] - dict_of_value["buy"]

        file_out.write(f"result,{result}\n")