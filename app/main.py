def create_report(data_file_name: str, report_file_name: str):
    supply, buy = 0, 0
    with open(data_file_name, "r") as file, open(report_file_name, "w") as out:
        for line in file:
            if "supply" in line:
                supply += int(line.split(",")[1].strip())
            else:
                buy += int(line.split(",")[1].strip())
        out.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply-buy}\n")
