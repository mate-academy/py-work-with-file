def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    with (open(data_file_name, "r") as input_data_file,
          open(report_file_name, "w") as report_file):
        input_lst = input_data_file.read().split()

        for i in input_lst:
            tmp_lst = i.split(",")
            if tmp_lst[0] == "supply":
                report_dict["supply"] += int(tmp_lst[1])
            if tmp_lst[0] == "buy":
                report_dict["buy"] += int(tmp_lst[1])
            report_dict["result"] = report_dict["supply"] - report_dict["buy"]

        for key, value in report_dict.items():
            content = f"{key},{value}\n"
            report_file.write(content)
