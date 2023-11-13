
def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        lines_dict = {}
        for line in file_in:
            if line:
                line_list = line.split(",")
                if line_list[0] not in lines_dict.keys():
                    lines_dict[line_list[0]] = int(line_list[1])
                else:
                    lines_dict[line_list[0]] += int(line_list[1])

        for key, value in lines_dict.items():
            file_out.write(f"{key},{value}\n")

        result = int(lines_dict["supply"]) - int(lines_dict["buy"])
        file_out.write(f"result,{result}")
