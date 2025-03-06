def create_report(data_file_name: str, report_file_name: str) -> None:
    file_data = open(data_file_name)
    res = [0, 0, 0]
    for i in file_data:
        if "supply" in i:
            res[0] += int(i.split(",")[1])
        elif "buy" in i:
            res[1] += int(i.split(",")[1])
    res[2] = res[0] - res[1]
    file_data.close()
    report_file_name = open(f"{report_file_name}", "w")
    report_file_name.write(f"supply,{str(res[0])}\n")
    report_file_name.write(f"buy,{str(res[1])}\n")
    report_file_name.write(f"result,{str(res[2])}\n")
    report_file_name.close()
