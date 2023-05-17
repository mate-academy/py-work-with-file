def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source_file:
        count_supply = 0
        count_buy = 0
        for line in source_file:
            text = line.replace("\n", "").split(",")
            print(text)
            if "supply" in text:
                count_supply += int(text[1])
            if "buy" in text:
                count_buy += int(text[1])
        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{count_supply}\n")
            report_file.write(f"buy,{count_buy}\n")
            report_file.write(f"result,{count_supply - count_buy}\n")
