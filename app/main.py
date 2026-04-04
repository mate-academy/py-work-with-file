def create_report(data_file_name: str, report_file_name: str) -> None:
    list_file_source = []
    with open(data_file_name, "r") as file_in:
        line_number = 1
        for line in file_in:
            work_dict = {}
            work_list = line.split(",")
            work_dict[work_list[0]] = int(work_list[1].rstrip())
            list_file_source.append(work_dict)
            line_number += 1
    summ_supply = 0
    summ_buy = 0
    for line_list in list_file_source:
        if "supply" in line_list:
            summ_supply += line_list["supply"]
        if "buy" in line_list:
            summ_buy += line_list["buy"]
    summ_result = summ_supply - summ_buy

    with open(report_file_name, "w") as file_out:
        file_out.write(f"supply,{summ_supply}\n")
        file_out.write(f"buy,{summ_buy}\n")
        file_out.write(f"result,{summ_result}\n")
