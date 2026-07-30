def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        supply = 0
        buy = 0
        for line in data_file:
            words = line.split(",")
            if words[0] == "supply":
                supply += int(words[1])
            elif words[0] == "buy":
                buy += int(words[1])
            else:
                pass
        report_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{supply - buy}\n")
