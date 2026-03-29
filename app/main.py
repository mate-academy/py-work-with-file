def create_report(data_file_name: str, report_file_name: str) -> None:
    buy: int = 0
    supply: int = 0
    with open(data_file_name, "r") as f_r:
        for line in f_r:
            split_arr = line.rsplit(",")
            split_arr[1] = split_arr[1].rstrip("\n")
            if split_arr[0] == "buy":
                buy += int(split_arr[1])
            else:
                supply += int(split_arr[1])
            result = supply - buy

    with open(report_file_name, "w") as f_w:
        f_w.write(f"supply,{supply}\n")
        f_w.write(f"buy,{buy}\n")
        f_w.write(f"result,{result}\n")
