def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file_in:
        buy = 0
        supply = 0
        for line in file_in.readlines():
            if "buy" in line:
                buy += int(line.split(",")[1])
            if "supply" in line:
                supply += int(line.split(",")[1])
    with open(report_file_name, "w") as file_out:
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}")
