def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        supply = 0
        buy = 0
        for line in file_in:
            line = line.replace("\n", "").split(",")
            if line[0] == "supply":
                supply += int(line[1])
            elif line[0] == "buy":
                buy += int(line[1])
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
