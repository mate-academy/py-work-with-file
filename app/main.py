def create_report(data_file_name: str, report_file_name: str) -> str:
    with open(data_file_name, "r") as f:
        supply = 0
        buy = 0
        for line in f:
            line = line.strip()
            if not line:
                continue

            list_word = line.split(",")

            if list_word[0] == "supply":
                supply += int(list_word[1])
            if list_word[0] == "buy":
                buy += int(list_word[1])

        result = supply - buy
        list_lines = [f"supply,{supply}", f"buy,{buy}", f"result,{result}"]
    with open(report_file_name, "w") as f:
        f.write("\n".join(list_lines) + "\n")
