def create_report(data_file_name: str, report_file_name: str) -> None:
    file_ = open(data_file_name, "r")
    buy_count = 0
    supply_count = 0
    for line in file_:
        if line != " ":
            data = line.split(",")
            name_ = data[0]
            count = int(data[1])
            if name_ == "buy":
                buy_count += count
            else:
                supply_count += count
    file_ = open(f"{report_file_name}", "a")
    first = f"{supply_count}\nbuy"
    second = f"{buy_count}\nresult"
    third = f"{supply_count - buy_count}\n"
    file_.write("supply," + first + "," + second + "," + third)
    file_.close()
