def create_report(data_file_name: str, report_file_name: str) -> None:
    file_read = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line in file_read:
        if line:
            product = line.split(",")
            product_number = int(product[1].strip())
            supply += product_number if product[0] == "supply" else 0
            buy += product_number if product[0] == "buy" else 0
    result = supply - buy
    file_read.close()
    file_append = open(report_file_name, "a")
    file_append.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
