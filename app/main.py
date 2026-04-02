def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name) as file_out,
          open(report_file_name, "w") as file_in):
        buy = 0
        supply = 0
        for line in file_out.readlines():
            line_list = line.split(",")
            if line_list[0] == "buy":
                buy += int(line_list[1])
            elif line_list[0] == "supply":
                supply += int(line_list[1])

        result = supply - buy

        file_in.write(f"supply,{supply}\n")
        file_in.write(f"buy,{buy}\n")
        file_in.write(f"result,{result}\n")
