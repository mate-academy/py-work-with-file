def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f, open(report_file_name, "w") as report:
        for data in f.read().split():
            if data.split(",")[0] == "supply":
                supply += int(data.split(",")[1])
            else:
                buy += int(data.split(",")[1])
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
