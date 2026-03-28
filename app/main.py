def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as f_in,
          open(report_file_name, "w") as f_out):
        content = f_in.readlines()
        data = {"supply": 0, "buy": 0}
        for line in content:
            if len(line):
                line_list = line.split(",")
                data[line_list[0]] += int(line_list[1])

        f_out.write(f"supply,{data['supply']}\n"
                    f"buy,{data['buy']}\n"
                    f"result,{data['supply'] - data['buy']}\n")
