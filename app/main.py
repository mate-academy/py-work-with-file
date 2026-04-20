def create_report(date_file_name:str, report_file_name:str) -> None:
    supply = 0
    buy = 0
    try:
        with open(date_file_name,"r") as file:
            for line in file:
                parts = line.strip().split(",")
                operation = parts[0]
                amount = int(parts[1])
                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount
    except FileNotFoundError:
        print("File not found")
        return

    result = (f"supply,{supply}\n"
              f"buy,{buy}\n"
              f"result,{supply - buy}\n"
              )
    with open(report_file_name, "w") as file:
        file.write(result)
