def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as input_file,
        open(report_file_name, "a") as output_file
    ):
        supply = 0
        buy = 0
        for line in input_file:
            line = line.split(",")
            if line[0] == "supply":
                supply += int(line[1])
            if line[0] == "buy":
                buy += int(line[1])
        result = supply - buy
        report = f"supply,{supply}\nbuy,{buy}\nresult,{result}\n"
        output_file.write(report)
