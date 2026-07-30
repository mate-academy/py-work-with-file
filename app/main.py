def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply_count = 0
    buy_count = 0
    with (open(data_file_name, "r") as origin,
          open(report_file_name, "w") as out):
        for current_line in origin.readlines():
            current_data = current_line.split(",")
            if len(current_data) == 2:
                command, count = current_data
                if command == "buy":
                    buy_count += int(count)
                elif command == "supply":
                    supply_count += int(count)
        out.write(f"supply,{supply_count}\n"
                  f"buy,{buy_count}\n"
                  f"result,{supply_count - buy_count}\n")
