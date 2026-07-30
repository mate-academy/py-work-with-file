def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file_in:
        data_dict = {}
        for line in file_in:
            if line != "\n":
                line_list = line.split()[0].split(",")
                if line_list[0] in data_dict:
                    data_dict[line_list[0]] += int(line_list[1])
                else:
                    data_dict[line_list[0]] = int(line_list[1])

        result = data_dict["supply"] - data_dict["buy"]

    with open(report_file_name, "w") as file_out:
        file_out.write(f"supply,{data_dict['supply']}\n")
        file_out.write(f"buy,{data_dict['buy']}\n")
        file_out.write(f"result,{result}\n")
