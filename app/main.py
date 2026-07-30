def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file_in, \
         open(report_file_name, "w+") as file_out:
        tabular_data = file_in.read()
        information = tabular_data.split("\n")
        data_list = []
        data_dict = dict()
        for info in information:
            if info:
                data_list.append(info.split(','))
        for data in data_list:
            if data[0] not in data_dict:
                data_dict[data[0]] = int(data[1])
            else:
                data_dict[data[0]] += int(data[1])
        operation_result = data_dict["supply"] - data_dict["buy"]
        written_info = f"supply,{data_dict['supply']}\n" \
                       f"buy,{data_dict['buy']}\n" \
                       f"result,{operation_result}\n"
        file_out.write(written_info)
