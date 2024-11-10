
def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "a") as file_out):
        data_file = file_in.read()
        data_file_list = data_file.split()
        for it in data_file_list:
            item = it.split(",")
            try:
                report_dict[item[0]]
            except KeyError:
                report_dict[item[0]] = int(item[1])
            else:
                report_dict[item[0]] += int(item[1])
        supply_value = report_dict["supply"]
        result = report_dict["supply"] - report_dict["buy"]
        file_out.write(f"supply,{supply_value}\n")
        file_out.write(f"buy,{report_dict["buy"]}\n")
        file_out.write(f"result,{result}\n")
