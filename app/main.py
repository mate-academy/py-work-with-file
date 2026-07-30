def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as in_file,
          open(report_file_name, "w") as out_file):
        supply = 0
        buy = 0
        for i in in_file.read().split("\n"):
            if i:
                product = i.split(",")
                if product[0] == "supply":
                    supply += int(product[1])
                elif product[0] == "buy":
                    buy += int(product[1])
        out_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
