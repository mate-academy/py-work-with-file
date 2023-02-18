def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(f"{data_file_name}", "r") as input_file:
        text = [pair.split(",") for pair in input_file.read().split()]

    supply = 0
    buy = 0

    for pair in text:
        if pair[0] == "supply":
            supply += int(pair[1])
        if pair[0] == "buy":
            buy += int(pair[1])

    result = supply - buy

    with open(f"{report_file_name}", "w") as output_file:
        output_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
