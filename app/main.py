def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as content:
        buy = 0
        supply = 0
        for words in content:
            buy_supply = words.split(",")
            if "buy" in buy_supply:
                buy += int(buy_supply[1])
            elif "supply" in buy_supply:
                supply += int(buy_supply[1])

        with open(report_file_name, "a") as writing_content:
            writing_content.write(
                f"supply,{supply}\n"
                f"buy,{buy}\n"
                f"result,{supply - buy}\n"
            )
