def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        data = data_file.read()
        data_split = data.split("\n")
        sum_buys = 0
        sum_supply = 0
        for words in data_split:
            if not words:
                continue
            word = words.split(",")
            if word[0] == "buy":
                sum_buys += int(word[1])
            if word[0] == "supply":
                sum_supply += int(word[1])
        result = sum_supply - sum_buys
        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{sum_supply}\n")
            report_file.write(f"buy,{sum_buys}\n")
            report_file.write(f"result,{str(result)}")
