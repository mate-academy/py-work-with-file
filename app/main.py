def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as input_file:
        split_spase_list = input_file.read().replace(",", "\n").split("\n")

    supply = 0
    buy = 0

    for pos in range(len(split_spase_list)):
        if split_spase_list[pos] == "supply":
            supply += int(split_spase_list[pos + 1])
        if split_spase_list[pos] == "buy":
            buy += int(split_spase_list[pos + 1])
    result = supply - buy
    with open(report_file_name, "w") as out_file:
        out_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
