def create_report(data_file_name: str, report_file_name: str) -> None:
    all_data = {}
    main_file = open(data_file_name)
    for line in main_file:
        row = line.replace("\n", "").split(",")
        if row[0] in all_data:
            all_data[row[0]] += int(row[1])
        else:
            all_data[row[0]] = int(row[1])
    result = all_data["supply"] - all_data["buy"]
    with open(report_file_name, "w") as f:
        f.write(f"supply,{all_data['supply']}\n"
                f"buy,{all_data['buy']}\n"
                f"result,{result}\n"
                )
