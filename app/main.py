def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as report):
        info = file_in.read().split("\n")
        buy, supply = 0, 0
        for i in info:
            if i.startswith("buy"):
                buy += int(i.split(",")[1])
            if i.startswith("supply"):
                i.split(",")
                supply += int(i.split(",")[1])

        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
