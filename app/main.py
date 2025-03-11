

def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}
    file_in = open(data_file_name, "r")
    for line in file_in.readlines():
        lis = line.strip().split(",")
        if lis[0] not in report_dict:
            report_dict[lis[0]] = int(lis[1])
        else:
            report_dict[lis[0]] += int(lis[1])

    file_in.close()
    report_dict["result"] = report_dict["supply"] - report_dict["buy"]
    file_out = open(report_file_name, "w")
    file_out.write(f"supply,{report_dict["supply"]}\n")
    file_out.write(f"buy,{report_dict["buy"]}\n")
    file_out.write(f"result,{report_dict["result"]}\n")
    file_out.close()
