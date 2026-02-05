def create_report(data_file_name:str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0, "result": 0}
    with (open(data_file_name, "r") as file_data,
          open(report_file_name, "w") as report_file
          ):
        line_list = file_data.readlines()

        for line in line_list:
            parsed_line = line.rstrip().split(",")
            item = parsed_line[0]
            item_amount = int(parsed_line[1])
            if item == "supply":
                report_dict["supply"] += item_amount
            if item == "buy":
                report_dict["buy"] += item_amount

        report_dict["result"] = report_dict["supply"] - report_dict["buy"]

        for item, item_amount in report_dict.items():
            report_file.write(f"{item},{item_amount}\n")
