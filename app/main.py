def create_report(data_file_name: str, report_file_name:str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        line_list = []
        supply = 0
        buy = 0
        for line in data_file:
            line_list = line.split(sep=",")
            if line_list[0] == "buy":
                buy += int(line_list[1])
            else:
                supply += int(line_list[1])
        result = supply - buy
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
