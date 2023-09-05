def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        buy = 0
        supply = 0
        for line in file_in:
            line = line.split(",")
            if "supply" in line:
                supply += int(line[1])
            else:
                buy += int(line[1])
        result = supply - buy
        file_out.write(f"supply,{supply}\n"
                       f"buy,{buy}\n"
                       f"result,{result}\n")
