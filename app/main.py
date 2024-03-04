def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file1, \
            open(report_file_name, "w") as file2:
        supply = 0
        buy = 0

        for line in file1.readlines():
            if line.split(",")[0] == "supply":
                supply += int(line.split(",")[1])
            if line.split(",")[0] == "buy":
                buy += int(line.split(",")[1])

        file2.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
