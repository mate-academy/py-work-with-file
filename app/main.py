def create_report(data_file_name: str, report_file_name: str) -> None:
    input_file = open(data_file_name, "r")
    data = input_file.read()
    words = {}
    for line in data.strip().split("\n"):
        parts = line.split(",")
        words[parts[0]] = words.get(parts[0], 0) + int(parts[-1])

    words["result"] = words["supply"] - words["buy"]
    order = ["supply", "buy", "result"]
    result = "".join(f"{key},{words[key]}\n" for key in order if key in words)
    print(result)
    with open(report_file_name, "w") as output_file :
        output_file.write(result)
