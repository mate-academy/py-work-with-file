def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as input_data_file:
        input_data_lines = input_data_file.readlines()

    result_report_dict = {}

    for line in input_data_lines:
        operation_type, amount = line.replace("\n", "").split(",")
        if operation_type in result_report_dict:
            result_report_dict[operation_type] += int(amount)
        else:
            result_report_dict[operation_type] = int(amount)

    result = result_report_dict["supply"] - result_report_dict["buy"]

    with open(report_file_name, "w") as output_data_file:
        output_data_file.write(f"supply,{result_report_dict['supply']}\n")
        output_data_file.write(f"buy,{result_report_dict['buy']}\n")
        output_data_file.write(f"result,{result}\n")
