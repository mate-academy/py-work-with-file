def create_report(data_file_name, report_file_name):
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        lines = data_file.readlines()

        for line in lines:
            if "supply" in line:
                supply += int(line.split(",")[1])
            elif "buy" in line:
                buy += int(line.split(",")[1])

    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
