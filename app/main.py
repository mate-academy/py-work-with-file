def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):

        data = data_file.read()

        supply = 0
        buy = 0

        for line in data.splitlines():
            line = line.replace("\n", "").replace("\r", "").split(",")
            if line[0] == "supply":
                supply += int(line[1])
            elif line[0] == "buy":
                buy += int(line[1])

        result = supply - buy

        report = f"supply,{supply}\nbuy,{buy}\nresult,{result}\n"
        report_file.write(report)
