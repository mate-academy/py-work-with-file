def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    counter = 0
    supply = 0
    buy = 0
    data_file = open(data_file_name)
    for line in data_file.readlines():
        if "buy" in line:
            data_file.read(4)
            if data_file.read(1).isnumeric():
                counter = +1
                if data_file.read(1).isnumeric():
                    counter =+ 1
                    if data_file.read(1).isnumeric():
                        counter =+ 1
                        if data_file.read(1).isnumeric():
                            counter += 1
            data_file.seek(4)
            buy += data_file.read(counter)
            counter = 0
    else:
        data_file.read(7)
        if data_file.read(1).isnumeric():
            counter =+ 1
            if data_file.read(1).isnumeric():
                counter =+ 1
                if data_file.read(1).isnumeric():
                    counter =+ 1
                    if data_file.read(1).isnumeric():
                        counter += 1
            data_file.seek(7)
            supply += data_file.read(counter)
            counter = 0
    data_file.close()
    file_report = open(report_file_name, "w")
    file_report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}")
    file_report.close()
