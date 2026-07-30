def create_report(data_file_name: str, report_file_name: str):
    numbers = "1234567890"
    supplys_count = 0
    buy_count = 0
    c = ''
    with open(data_file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            if 'supply' in line:
                for i in line:
                    if i in numbers:
                        c += i
                supplys_count += int(c)
                c = ''
    with open(data_file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            if 'buy' in line:
                for i in line:
                    if i in numbers:
                        c += i
                buy_count += int(c)
                c = ''
    result = supplys_count - buy_count
    with open(report_file_name, 'w') as f:
        f.write(f"supply,{supplys_count}\n")
        f.write(f"buy,{buy_count}\n")
        f.write(f"result,{result}\n")
