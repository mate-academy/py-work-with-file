def create_report(data_file_name: str, report_file_name:str) -> None:
    with open(data_file_name,"r") as infile:
        supply = 0
        buy = 0

        for line in infile:
            line = line.strip()

            if not line:
                continue

            op,amount_str = line.split(",")
            amount = int(amount_str)

            if op == "supply":
                supply += amount
            elif op == "buy":
                buy += amount

        result = supply - buy

    with open(report_file_name,"w",) as outfile:
        outfile.write(f"supply,{supply}\n")
        outfile.write(f"buy,{buy}\n")
        outfile.write(f"result,{result}\n")
