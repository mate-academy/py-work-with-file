def create_report(data_file_name: str, report_file_name: str) -> None:

    file = open(data_file_name, "r")
    new_supply = 0
    new_buy = 0

    for row in file:
        row = row.strip().split(",")
        if row[0] == "supply":
            new_supply += int(row[1])
        elif row[0] == "buy":
            new_buy += int(row[1])

    file.close()

    file2 = open(report_file_name,"w")
    file2.write(f"supply,{new_supply}\n")
    file2.write(f"buy,{new_buy}\n")
    file2.write(f"result,{new_supply - new_buy}\n")

    file2.close()