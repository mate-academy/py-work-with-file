def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    result_dict = {}
    with (open(data_file_name, "r") as data,
          open(report_file_name, "a") as report):
        lines = data.readlines()
        print(lines)
        for line in lines:
            key, value = line.split(",")
            print(key, value)
            if key in result_dict:
                result_dict[key] += int(value.strip())
            else:
                result_dict[key] = int(value.strip())
        report.write(f"supply,{result_dict['supply']}\n")
        report.write(f"buy,{result_dict['buy']}\n")
        report.write(f"result,{result_dict['supply'] - result_dict['buy']}\n")
