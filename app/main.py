def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data:
        with open(report_file_name, "w") as report:
            temp_dict = {"supply": 0, "buy": 0, "result": 0}
            for line in data.readlines():
                current_line = line.split(",")
                if current_line[0] == "supply":
                    new_val = temp_dict["supply"] + int(current_line[1])
                    temp_dict["supply"] = new_val
                elif current_line[0] == "buy":
                    new_val = temp_dict["buy"] + int(current_line[1])
                    temp_dict["buy"] = new_val
            temp_dict["result"] = temp_dict["supply"] - temp_dict["buy"]
            for key, value in temp_dict.items():
                report_line = f"{key},{value}\n"
                report.write(report_line)
