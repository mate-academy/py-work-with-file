def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {}
    with open(data_file_name, "r") as first_file:
        for line in first_file:
            line_split = line.split(",")
            line_dict = {line_split[0]: int(line_split[1])}
            for key, value in line_dict.items():
                if key in (line_dict and result_dict):
                    result_dict[key] += line_dict[key]
                else:
                    result_dict[key] = value
        result_dict["result"] = result_dict["supply"] - result_dict["buy"]
    supply = f"supply,{result_dict['supply']}"
    buy = f"buy,{result_dict['buy']}"
    result = f"result,{result_dict['result']}"
    report = f"{supply}\n{buy}\n{result}\n"
    with open(report_file_name, "w") as second_file:
        second_file.write(report)
