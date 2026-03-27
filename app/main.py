def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data, \
            open(report_file_name, "w") as report:
        lines = []
        result_ls = []
        for line in data:
            lines.append(line)
        if lines[-1] == "":
            lines = lines[0:-1]
        supply = 0
        buy = 0
        for line in lines:
            if "supply" in line:
                ls = line.split(",")
                supply += int(ls[1])
                ls.clear()
            if "buy" in line:
                ls = line.split(",")
                buy += int(ls[1])
                ls.clear()
        result = supply - buy
        result_line1 = "supply," + str(supply)
        result_line2 = "buy," + str(buy)
        result_line3 = "result," + str(result)
        result_ls.append(result_line1)
        result_ls.append(result_line2)
        result_ls.append(result_line3)

        for line in result_ls:
            report.write(line + "\n")
