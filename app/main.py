def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0
    with (open(data_file_name, "r") as source,
          open(report_file_name, "w") as target):
        for line in source:
            if line.split(",")[0] == "supply":
                supply += int(line.split(",")[1])
            if line.split(",")[0] == "buy":
                buy += int(line.split(",")[1])

        target.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{supply - buy}\n")
