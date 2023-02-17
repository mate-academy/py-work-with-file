def create_report(data_file_name: str, report_file_name: str) -> None:
    buy, supply = 0, 0
    with open(data_file_name) as fr:
        for line in fr.readlines():
            command, price = line.split(",")
            if command == "buy":
                buy += int(price)
            elif command == "supply":
                supply += int(price)

    with open(report_file_name, "w") as fw:
        fw.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
