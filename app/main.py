def create_report(data_file_name: str, report_file_name: str) -> None:
    f_products = open(data_file_name, "r")
    supply = 0
    buy = 0
    for product in f_products:
        product_l = product.strip("\n").split(",")
        if product_l[0] == "supply":
            supply += int(product_l[1])
        elif product_l[0] == "buy":
            buy += int(product_l[1])
    result = supply - buy
    w_file = open(report_file_name, "w")
    w_file.write(f"supply,{supply}\n")
    w_file.write(f"buy,{buy}\n")
    w_file.write(f"result,{result}\n")
