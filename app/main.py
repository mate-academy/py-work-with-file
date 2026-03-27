def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):
        data_dict = {}
        for line in file_in:
            line_split = line.split(",")
            if line_split[0] not in data_dict:
                data_dict[f"{line_split[0]}"] = int(line_split[1])
            elif line_split[0] in data_dict:
                data_dict[line_split[0]] += int(line_split[1])
        supply = data_dict["supply"]
        buy = data_dict["buy"]
        result = supply - buy
        file_out.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{result}\n"
        )
