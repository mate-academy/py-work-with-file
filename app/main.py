def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        content = file_in.read().split("\n")
        for i in range(len(content) - 1):
            content_list = content[i].split(",")
            if content_list[0] == "supply":
                supply += int(content_list[1])
            if content_list[0] == "buy":
                buy += int(content_list[1])
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply-buy}\n")
