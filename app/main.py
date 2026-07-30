def create_report(data_file_name: str, report_file_name: str) -> None:
    content = {"supply": 0, "buy": 0}
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        for line in data_file.readlines():
            name, value = line.split(",")
            content[name] += int(value)
        report_file.write(f"supply,{content['supply']}\n"
                          f"buy,{content['buy']}\n"
                          f"result,{content['supply'] - content['buy']}\n")
