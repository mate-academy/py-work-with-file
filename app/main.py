def create_report( data_file_name: str, report_file_name: str):
    supply, buy = 0, 0
    with open(data_file_name, 'r', encoding='utf-8') as data_file:
        for item in data_file.readlines():
            actions, price =  item.replace("\n", "").split(",")
            if actions == "supply":
                supply += int(price)
            elif actions == "buy":
                buy += int(price)
        result = int(supply) - int(buy)

    with open(report_file_name, "w") as rf:
        rf.write(f"supply,{supply}\n")
        rf.write(f"buy,{buy}\n")
        rf.write(f"result,{result}\n")
