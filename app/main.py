def create_report(data_file_name: str, report_file_name: str) -> None:
    enter_file = open(data_file_name)
    new_dict = {}
    for line in enter_file.readlines():
        line_in_list = line.rstrip("\n").split(",")
        if line_in_list[0] not in new_dict:
            new_dict.update({line_in_list[0]: int(line_in_list[1])})
        elif line == "":
            continue
        else:
            new_dict[line_in_list[0]] += int(line_in_list[1])

    enter_file.close()

    supply = int(new_dict["supply"])
    buy = int(new_dict["buy"])
    result = supply - buy
    new_dict.update({"result": result})

    report_file = open(report_file_name, "w")

    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")
    report_file.close()
