def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    counter = 0
    supply = 0
    buy = 0
    file = open(data_file_name)
    for line in file.readlines():
        if "buy" in line:
            file.read(4)
            if file.read(1).isnumeric():
                counter =+ 1
                if file.read(1).isnumeric():
                    counter =+ 1
                    if file.read(1).isnumeric():
                        counter =+ 1
                        if file.read(1).isnumeric():
                            counter += 1
            file.seek(4)
            buy += file.read(counter)
            counter = 0
        else:
            file.read(7)
            if file.read(1).isnumeric():
                counter =+ 1
                if file.read(1).isnumeric():
                    counter =+ 1
                    if file.read(1).isnumeric():
                        counter =+ 1
                        if file.read(1).isnumeric():
                            counter += 1
            file.seek(7)
            supply += file.read(counter)
            counter = 0
    file.close()
    file_report = open(report_file_name, "w")
    file_report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}")
    file_report.close()
