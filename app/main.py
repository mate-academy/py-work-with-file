def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    result = 0
    with open(data_file_name, "r") as file_in, \
         open(report_file_name, "w") as file_out:
        reader = file_in.readlines()
        for row in reader:
            row = row.split(",")
            if row[0] == "supply":
                supply += int(row[1])
            if row[0] == "buy":
                buy += int(row[1])
            result = supply - buy
        file_out.write(f"supply,{supply}\n"
                       f"buy,{buy}\n"
                       f"result,{result}\n")
