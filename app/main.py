def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0

    with open(data_file_name, "r") as f, open(report_file_name, "w") as f1:
        file_info = f.readlines()
        for row in file_info:
            line = row.split(",")
            if line[0] == "supply":
                supply += int(line[1])
            elif line[0] == "buy":
                buy += int(line[1])
            result = supply - buy

        f1.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
