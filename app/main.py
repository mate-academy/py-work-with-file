def create_report(data_file_name: str, report_file_name: str) -> None:
    output_data = {}

    input_file = open(data_file_name)
    for line in input_file:
        key, value = line.strip().split(",")
        output_data[key] = output_data.get(key, 0) + int(value)
    input_file.close()

    output_file = open(report_file_name, "w")
    output_file.write(f"supply,{output_data['supply']}\n")
    output_file.write(f"buy,{output_data['buy']}\n")
    output_file.write(f"result,{output_data['supply'] - output_data['buy']}\n")
    output_file.close()
