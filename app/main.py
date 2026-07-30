def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        content = f.read()

    supply = 0
    buy = 0
    for line in content.strip().split("\n"):
        if line:
            parts = line.split(",")
            operation = parts[0]
            amount = int(parts[1])
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount
    result = supply - buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
