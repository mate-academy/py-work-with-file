def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_info = {}
    with (open(data_file_name, "r") as read_file,
          open(report_file_name, "w") as file):
        for item in read_file:
            item, count = item[:-1].split(",")
            if item not in dict_info:
                dict_info[item] = int(count)
            else:
                dict_info[item] += int(count)
        file.write(f"supply,{dict_info['supply']}\n")
        file.write(f"buy,{dict_info['buy']}\n")
        file.write(f"result,{dict_info['supply'] - dict_info['buy']}\n")
