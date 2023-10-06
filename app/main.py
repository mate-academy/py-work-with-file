def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as text:
        data = text.readlines()
        for info in range(len(data)):
            data[info] = data[info].strip()
        new_dict = {}
        for info in data:
            info = info.split(",")
            if info[0] in new_dict:
                new_dict[info[0]] += int(info[1])
            else:
                new_dict[info[0]] = int(info[1])
        new_dict["result"] = new_dict["supply"] - new_dict["buy"]
    with open(report_file_name, "w") as report:
        report.write(f'supply,{new_dict["supply"]}\n')
        report.write(f'buy,{new_dict["buy"]}\n')
        report.write(f'result,{new_dict["result"]}\n')
