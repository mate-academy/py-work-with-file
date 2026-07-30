def create_report(data_file_name: str, report_file_name: str) -> None:

    buy, supply, result = 0, 0, 0
    with open(data_file_name, "r") as fo:
        for line in fo.readlines():
            line_list = line.split(",")

            if line_list[0] == "buy":
                buy += int(line_list[1])
            elif line_list[0] == "supply":
                supply += int(line_list[1])
        result = supply - buy

    with open(report_file_name, "w") as fw:
        fw.write(f"supply,{supply}\n")
        fw.write(f"buy,{buy}\n")
        fw.write(f"result,{result}\n")
