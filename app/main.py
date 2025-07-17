def create_report(data_file_name: str, report_file_name: str) -> None:
    my_file = open(data_file_name)
    my_dict = {}
    for line in my_file.readlines():
        if len(line) == 0:
            continue
        values = line.split(",")
        label, value = values
        if label not in my_dict:
            my_dict[label] = int(value)
        else:
            my_dict[label] += int(value)
    my_file.close()
    my_file = open(report_file_name, "w")
    my_file.write(f"supply,{my_dict['supply']}\n")
    my_file.write(f"buy,{my_dict['buy']}\n")
    diff = my_dict["supply"] - my_dict["buy"]
    my_file.write(f"result,{diff}\n")
    my_file.close()
