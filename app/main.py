def create_report(data_file_name: str, report_file_name: str):
    supply_ = 0
    buy_ = 0
    with open(data_file_name, "r") as f1, open(report_file_name, "w") as f2:
        report = f1.readlines()
        for line in report:
            line_ = line.split(",")
            if line_[0] == "supply":
                supply_ += int(line_[1])
            else:
                buy_ += int(line_[1])

        f2.write("supply," + str(
            supply_) + "\n" + "buy," + str(
            buy_) + "\nresult," + str(supply_ - buy_) + "\n")
