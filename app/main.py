def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):

        for line in data_file.readlines():
            line = line.split(",")
            if line[0] == "supply":
                supply += int(line[1])
            else:
                buy += int(line[1])

        report_file.write(f"supply,{supply}\nbuy,{buy}\n"
                          f"result,{supply - buy}\n")
