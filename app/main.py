def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {"supply": 0, "buy": 0}
    input_file = open(data_file_name, "r")
    for line in input_file:
        if not line.strip():
            continue
        operation, amount_str = line.strip().split(",")
        amount = int(amount_str)
        if operation == "buy":
            result_dict["buy"] += amount
        elif operation == "supply":
            result_dict["supply"] += amount
    input_file.close()

    result = result_dict["supply"] - result_dict["buy"]

    output_file = open(report_file_name, "w")
    output_file.write(f"supply,{result_dict['supply']}\n")
    output_file.write(f"buy,{result_dict['buy']}\n")
    output_file.write(f"result,{result}\n")
    output_file.close()
