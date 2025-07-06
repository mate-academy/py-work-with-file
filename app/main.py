
def create_report(data_file_name: str, report_file_name: str) -> None:
    fr = open(data_file_name, "r")
    fw = open(report_file_name, "w")
    new_dict = {}

    for line in fr:
        items = line.lower().strip().split(",")
        if items[0] in new_dict:
            new_dict[items[0]] += int(items[1])
        else:
            new_dict[items[0]] = int(items[1])

    fw.write(f"supply,{new_dict["supply"]}\n")
    fw.write(f"buy,{new_dict["buy"]}\n")
    fw.write(f"result,{new_dict["supply"] - new_dict["buy"]}\n")

    fr.close()
    fw.close()
