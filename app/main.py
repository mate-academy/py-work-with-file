def create_report(data_file_name: str, report_file_name: str):
    supply, buy = 0, 0

    with open(data_file_name, "r") as data_file:
        for line in data_file.read().split("\n"):
            if line != "":
                operation, volume = line.split(",")
                if operation == "supply":
                    supply += int(volume)
                if operation == "buy":
                    buy += int(volume)
            with open(report_file_name, "w") as report_file:
                report_file.write(f"supply,{supply}\nbuy,"
                                  f"{buy}\nresult,{supply - buy}\n")
