def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as first_file:
        for line in first_file:
            if line.strip():
                action, value = line.split(",")
                result_dict[action.strip()] += int(value.strip())

    result = result_dict["supply"] - result_dict["buy"]
    with open(report_file_name, "w") as second_file:
        second_file.write(f"supply,{result_dict['supply']}\n")
        second_file.write(f"buy,{result_dict['buy']}\n")
        second_file.write(f"result,{result}\n")
