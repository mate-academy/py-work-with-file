def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as r_file:
        result_dict = {}

        for line in r_file:
            line_list = line.rstrip("\n").split(",")
            if line_list[0] in result_dict:
                result_dict[line_list[0]] += int(line_list[1])
            else:
                result_dict[line_list[0]] = int(line_list[1])

    result = [
        f'supply,{result_dict["supply"]}\n',
        f'buy,{result_dict["buy"]}\n',
        f'result,{result_dict["supply"] - result_dict["buy"]}\n'
    ]

    with open(report_file_name, "w") as w_file:
        w_file.write("".join(result))
