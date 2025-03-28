def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with (open(data_file_name, "r") as f_out,
          open(report_file_name, "w") as f_in):
        items = f_out.read().split()
        for item in items:

            for i in item.split(","):
                if i == "supply":
                    supply += int(item.split(",")[1])
                elif i == "buy":
                    buy += int(item.split(",")[1])
        f_in.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
