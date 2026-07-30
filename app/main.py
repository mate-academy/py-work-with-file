def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, 'r') as file, \
            open(report_file_name, 'w') as new_file:
        supply = 0
        buy = 0
        for line in file.readlines():
            if "supply" in line:
                supply += int(line.split(",")[1])
            else:
                buy += int(line.split(",")[1])
        new_file.write(f"supply,{supply}\n"
                       f"buy,{buy}\n"
                       f"result,{supply - buy}\n")
