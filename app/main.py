def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply = 0
    buy = 0

    for line in data_file.readlines():
        line_ls = line.split(",")
        amount = int(line_ls[1])
        if line_ls[0] == "supply":
            supply += amount
        elif line_ls[0] == "buy":
            buy += amount
        else:
            print("Unable to sum the quantity")

    data_file.close()

    result = supply - buy

    tags = ["supply", "buy", "result"]
    values = [supply, buy, result]

    for tag, value in zip(tags, values):
        new_file = open(report_file_name, "a")
        new_file.write(f"{tag},{value}\n")

    new_file.close()
