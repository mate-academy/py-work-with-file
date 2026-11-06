def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    input_file = open(data_file_name)
    data_to_write = {"supply": 0, "buy": 0}
    for line in input_file:
        line_desc = line.split(",")[0]
        line_num = int(line.split(",")[1])
        data_to_write[line_desc] += line_num
    input_file.close()
    output_file = open(report_file_name, "w")
    print(f"supply,{data_to_write['supply']}", file=output_file)
    print(f"buy,{data_to_write['buy']}", file=output_file)
    print(f"result,{data_to_write['supply'] - data_to_write['buy']}",
          file=output_file)
    output_file.close()
