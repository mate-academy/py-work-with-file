def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        for line in data_file:
            temp_list = line.split(",")
            if temp_list[0] == "supply":
                supply += int(temp_list[1])
            if temp_list[0] == "buy":
                buy += int(temp_list[1])
        report_file.write(f"supply,{supply}\nbuy,"
                          f"{buy}\nresult,{supply - buy}\n")
