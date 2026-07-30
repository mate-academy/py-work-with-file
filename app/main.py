def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as f_in,
          open(report_file_name, "w") as f_out):
        supply = 0
        buy = 0
        for line in f_in:
            line = line.replace("\n", "").split(",")
            if line[0] == "supply":
                supply += int(line[1])
            elif line[0] == "buy":
                buy += int(line[1])
        f_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
