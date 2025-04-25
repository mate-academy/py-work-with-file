def create_report(data_file_name: str, report_file_name: str) -> None:
    words = {}
    with open(data_file_name, "r") as input_file:
        for line in input_file:
            action, amount = line.strip().split(",")
            words[action] = words.get(action, 0) + int(amount)

    words["result"] = words["supply"] - words["buy"]

    with open(report_file_name, "w") as output_file:
        for key in ["supply", "buy", "result"]:
            output_file.write(f"{key},{words[key]}\n")
