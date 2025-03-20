def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}
    with open(data_file_name, "r") as st:
        for product in st:
            product, number = product[:-1].split(",")
            if product not in result:
                result[product] = int(number)
            else:
                result[product] += int(number)
    with open(report_file_name, "a") as rp:
        rp.write(f"supply,{result['supply']}\n")
        rp.write(f"buy,{result['buy']}\n")
        rp.write(f"result,{result['supply'] - result['buy']}\n")
