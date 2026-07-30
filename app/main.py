def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        lines_dict = {"buy": 0, "supply": 0}
        for line in file_in:
            if line:
                line_list = line.split(",")
                if line_list[0] == "buy":
                    lines_dict["buy"] += int(line_list[1])
                elif line_list[0] == "supply":
                    lines_dict["supply"] += int(line_list[1])

        result = int(lines_dict["supply"]) - int(lines_dict["buy"])

        file_out.writelines([f"supply,{lines_dict['supply']}\n",
                             f"buy,{lines_dict['buy']}\n",
                             f"result,{result}\n"])
