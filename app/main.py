def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name) as initial_file,
          open(report_file_name, "a") as res_file):
        supply = 0
        buy = 0
        for line in initial_file:
            line = line.split(",")
            if line[0] == "supply":
                supply += int(line[1])
            else:
                buy += int(line[1])
        res_file.write("supply," + str(supply) + "\n")
        res_file.write("buy," + str(buy) + "\n")
        res_file.write("result," + str(supply - buy) + "\n")
