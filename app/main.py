def create_report(data_file_name: str, report_file_name: str) -> None:
    file_input = open(data_file_name, "r")
    file_output = open(report_file_name, "a")
    sum_of_items = {}
    for line in file_input.readlines():
        line_list = line.rstrip("\n").split(",")
        if line_list[0] not in sum_of_items:
            sum_of_items.update({line_list[0]: line_list[1]})
        else:
            item_count = (int(sum_of_items.get(line_list[0]))
                          + int(line_list[1]))
            sum_of_items.update({line_list[0]: item_count})
    file_output.write(f"supply,{sum_of_items.get("supply")}\n")
    file_output.write(f"buy,{sum_of_items.get("buy")}\n")
    result = int(sum_of_items["supply"]) - int(sum_of_items["buy"])
    file_output.write(f"result,{result}\n")
    file_input.close()
    file_output.close()
