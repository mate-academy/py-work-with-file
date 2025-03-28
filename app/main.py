
def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as d, open(report_file_name, "w") as r:
        content = d.readlines()
        for line in content:
            if "supply" == line.split(',')[0]:
                supply += int(line.split(',')[1])
            elif "buy" == line.split(',')[0]:
                buy += int(line.split(',')[1])
        result = supply - buy
        r.write(f"{'supply'},{supply}\n"
                f"{'buy'},{buy}\n"
                f"{'result'},{result}\n")
