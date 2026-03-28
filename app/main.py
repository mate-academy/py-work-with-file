def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        dic = {}
        for line in data_file.readlines():
            key, value = line.split(",")
            dic[key] = dic.get(key, 0) + int(value)

        report_file.write(f"supply,{dic['supply']}\n")
        report_file.write(f"buy,{dic['buy']}\n")
        report_file.write(f"result,{dic['supply'] - dic['buy']}\n")
