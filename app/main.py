def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open("../" + data_file_name, "r") as data_file:
        chunks = data_file.readlines()
        for chunk in chunks:
            split_chunk = chunk.split(",")
            if split_chunk[0] == "buy":
                buy += int(split_chunk[1])
            if split_chunk[0] == "supply":
                supply += int(split_chunk[1])

        result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.write(str(f"supply,{supply}\n"
                              f"buy,{buy}\n"
                              f"result,{result}\n"))
