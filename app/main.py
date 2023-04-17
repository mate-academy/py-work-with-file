def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as save_file
    ):
        read_line = data_file.read()
        suplly_total = 0
        buy_total = 0
        for word in read_line.split():
            if word.startswith("supply"):
                suplly_total += int(word.split(",")[1])
            if word.startswith("buy"):
                buy_total += int(word.split(",")[1])
        save_file.write(
            f"supply,{suplly_total}\n"
            f"buy,{buy_total}\n"
            f"result,{suplly_total - buy_total}\n"
        )
