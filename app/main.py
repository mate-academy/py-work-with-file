def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        supply_total = 0
        buy_total = 0
        for line in file:
            if line.strip() != "":
                parts = line.strip().split(",")
                if parts[0] == "supply":
                    supply_total += int(parts[1])
                else:
                    buy_total += int(parts[1])
        file.close()
        file_res = open(report_file_name, "w")
        file_res.write(f"supply,{supply_total}\n")
        file_res.write(f"buy,{buy_total}\n")
        file_res.write(f"result,{supply_total - buy_total}\n")
        file_res.close()
