def create_report(data_file_name: str, report_file_name: str) -> None:
    data = open(data_file_name)
    supply = 0
    buy = 0
    for line in data:
        prepared_line = line.strip()
        arr = prepared_line.split(",")
        if "supply" in arr:
            supply += int(arr[1])
        if "buy" in arr:
            buy += int(arr[1])

    report_data = ("supply" + ","
                   + f"{supply}\nbuy" + ","
                   + f"{buy}\nresult" + ","
                   + f"{supply - buy}\n")
    report = open(report_file_name, 'w')
    report.write(report_data)
    data.close()
    report.close()
