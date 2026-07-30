def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as new_data_file_name:
        supply = 0
        buy = 0
        for word in new_data_file_name:
            word_ = word.split(",")
            if word_[0] == "supply":
                supply += int(word_[1])
            if word_[0] == "buy":
                buy += int(word_[1])
    with open(report_file_name, "w") as upgrade_report_file_name:
        upgrade_report_file_name.write(f"supply,{supply}\n"
                                       f"buy,{buy}\n"
                                       f"result,{supply - buy}\n")
