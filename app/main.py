def create_report(data_file_name: str, report_file_name: str = None) -> None:
    with open(data_file_name) as f:
        supply = sum(int(line.split(",")[1].rstrip())
                     for line in f.readlines()
                     if line.split(",")[0] in "supply")
        f.seek(0)
        buy = sum(int(line.split(",")[1].rstrip())
                  for line in f.readlines() if line.split(",")[0] in "buy")
    report = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
    with open(report_file_name, "w") as g:
        g.write(report)
