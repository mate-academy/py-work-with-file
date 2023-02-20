def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as f_first:
        supply = 0
        buy = 0
        for line in f_first:
            if line.split(",")[0] == "supply":
                supply += int(line.split(",")[1])
            if line.split(",")[0] == "buy":
                buy += int(line.split(",")[1])
        result = supply - buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
