def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_data,
          open(report_file_name, "w") as file_report):
        supply = 0
        buy = 0
        for line in file_data:
            if line.split(",")[0] == "supply":
                supply += line.split(",")[1]
            elif line.split(",")[0] == "buy":
                supply += line.split(",")[1]
        result = supply - buy
        file_report.write(f"supply, {supply}\nbuy, {buy}\nresult, {result}")
