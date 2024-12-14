def craeate_report(date_file_name: str, report_file_name: str) -> None:
    date_file = open(date_file_name, "r")
    supply = 0
    buy = 0
    for line in date_file:
        name = line.split(",")
        if "supply" in name:
            supply += name[1]
        elif "buy" in name:
            buy += name[1]

    with open(report_file_name, "w"):
        report_file_name.write(f"supply, {supply}\n"
                               f"buy, {buy}\n"
                               f"result, {supply - buy}")
