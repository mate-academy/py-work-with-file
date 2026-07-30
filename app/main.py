def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    file_in = open(data_file_name, "r")
    operation = file_in.read().split("\n")
    file_in.close()

    for i in operation:
        if i == "":
            continue
        parse = i.split(",")
        if parse[0] == "supply":
            supply += int(parse[1])
        else:
            buy += int(parse[1])

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")


if __name__ == "__main__":
    create_report("apples.csv", "")
