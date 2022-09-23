def create_report(data_file_name: str, report_file_name: str):
    buy = 0
    supply = 0
    with open(data_file_name, "r") as file_in, \
            open(report_file_name, "w") as file_out:
        for line in file_in:
            key, value = line.split(",")
            if key == "buy":
                buy += int(value)
            if key == "supply":
                supply += int(value)
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
