def create_report(data_file_name: str,
                  report_file_name: str
                  ) -> None:
    with open(data_file_name, "r") as data_f, \
            open(report_file_name, "w") as report_f:
        supply = 0
        buy = 0
        for row in data_f:
            if "supply" in row.split(","):
                supply += int(row.split(",")[1])
            if "buy" in row.split(","):
                buy += int(row.split(",")[1])
        result = supply - buy
        report_f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
