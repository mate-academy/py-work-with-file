def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as text:
        for line in text:
            line_as_list = line.split(",")
            if "supply" == line_as_list[0]:
                supply += int(line_as_list[1])
            if "buy" == line_as_list[0]:
                buy += int(line_as_list[1])
    with open(report_file_name, "w") as text:
        text.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
