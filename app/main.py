def create_report(data_file_name: str, report_file_name: str):
    supply, buy = 0, 0

    with open(data_file_name, "r") as data_file:
        with open(report_file_name, "w") as report_file:
            data = data_file.read().split("\n")
            for line in data:
                if line != "":
                    operation, volume = line.split(",")
                    if operation == "supply":
                        supply += int(volume)
                    if operation == "buy":
                        buy += int(volume)

            report = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
            report_file.write(report)

            report_file.close()
            data_file.close()
