def create_report(data_file_name: str, report_file_name: int):
    buy = 0
    supply = 0
    with open(data_file_name, "r") as file:
        arr = sorted(file.readlines())
        for item in arr:
            if item[0] == "b":
                buy += int(''.join([num for num in item if num.isdigit()]))
            else:
                supply += int(''.join([num for num in item if num.isdigit()]))

    with open(f"{report_file_name}", "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
