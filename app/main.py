def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as reading_file:
        suply = 0
        buy = 0
        for line in reading_file.readlines():
            if "buy" in line:
                buy += int(line.split(",")[1])
            if "suply" in line:
                buy += int(line.split(",")[1])
    with open(report_file_name, "w") as writing_file:
        writing_file.write(f"supply,{suply}\nbuy,{buy}\nresult,{suply-buy}\n")