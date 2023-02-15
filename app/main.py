def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {}
    with open(data_file_name, "r") as raw_data:
        for line in raw_data:
            if line:
                operation_type, amount = line.split(",")
                value = result_dict.setdefault(operation_type, [0])
                value[0] += int(amount)

    result_dict["result"] = result_dict["supply"][0] - result_dict["buy"][0]

    with open(report_file_name, "w") as final_data:
        final_data.write(f"supply,{str(result_dict['supply'][0])}\n")
        final_data.write(f"buy,{str(result_dict['buy'][0])}\n")
        final_data.write(f"result,{str(result_dict['result'])}\n")
