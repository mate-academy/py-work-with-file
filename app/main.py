def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f:
        text = f.read()
        text = text.replace("\n", " ")
        words = text.split(" ")
        for symbol in words:
            new_words = symbol.split(",")
            if new_words[0] == "supply":
                supply += int(new_words[1])
            if new_words[0] == "buy":
                buy += int(new_words[1])
        result = supply - buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
