def create_report(data_file_name, report_file_name):
    with open(data_file_name, "r") as file_in:
        supply = 0
        buy = 0
        result = 0
        for line in file_in.readlines():
            if line.split(",")[0] == "supply":
                supply += int(line.split(",")[1])
            else:
                buy += int(line.split(",")[1])
        result = supply - buy
    with open(report_file_name, "w") as file_out:
        file_content = \
            "supply," + str(supply) + '\n' + \
            "buy," + str(buy) + '\n' + \
            "result," + str(result) + '\n'
        file_out.write(file_content)
