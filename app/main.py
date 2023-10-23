def check_digit(word: str) -> int:
    res = ""
    for i in range(len(word)):
        if word[i].isdigit():
            res += word[i]
    if res == "":
        return 0
    return int(res)


def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    with (
        open(data_file_name, "r",) as data_file,
        open(report_file_name, "w") as report_file
    ):
        supply = 0
        buy = 0
        for line in data_file:
            if "buy" in line:
                buy += check_digit(line)
            if "supply" in line:
                supply += check_digit(line)
        report_file.write("supply," + str(supply) + "\n")
        report_file.write("buy," + str(buy) + "\n")
        report_file.write("result," + str(supply - buy) + "\n")
