def create_report(data_file_name: str, report_file_name: str) -> None:
    work_dict = {}
    with open(data_file_name, "r") as data_file:
        for value in data_file.readlines():
            my_key, my_val = value.split(",")
            if my_key not in work_dict:
                work_dict[my_key] = int(my_val)
            else:
                work_dict[my_key] += int(my_val)

    with open(report_file_name, "w") as direct_file:
        direct_file.write(f"supply,{work_dict['supply']}\n")
        direct_file.write(f"buy,{work_dict['buy']}\n")
        direct_file.write(f"result,{work_dict['supply'] - work_dict['buy']}\n")
