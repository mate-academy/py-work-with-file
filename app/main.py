def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name, "r") as s_file:
        for i in s_file.read().split():
            ls = i.split(",")

            if ls[0] == "buy":
                buy += int(ls[1])
            else:
                supply += int(ls[1])
    result = supply - buy
    str_result = f"supply,{supply}\nbuy,{buy}\nresult,{result}\n"
    with open(report_file_name, "w") as d_file:
        d_file.write(str_result)
