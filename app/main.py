def create_report(date_file_name: str, report_file_name: str) -> None:
    date_file = open(date_file_name, "r")
    supply = 0
    buy = 0
    for line in date_file:
        name = line.split(",")
        if "supply" in name:
            supply += int(name[1])
        elif "buy" in name:
            buy += int(name[1])
    date_file.close()
    new_file_name = open(report_file_name, "w")
    new_file_name.write(f"supply,{supply}\n"
                        f"buy,{buy}\n"
                        f"result,{supply - buy}")
    new_file_name.close()
