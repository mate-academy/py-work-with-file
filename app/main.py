def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file_read:
        for line in file_read:
            if line:
                temp = line.split(",")
                if "supply" in temp:
                    supply += int(temp[1])
                elif "buy" in temp:
                    buy += int(temp[1])
    with open(report_file_name, "w") as file_write:
        file_write.write(f"supply,{supply}\n")
        file_write.write(f"buy,{buy}\n")
        file_write.write(f"result,{supply - buy}\n")
