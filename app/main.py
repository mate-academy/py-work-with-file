

def create_report(data_file_name: str, report_file_name: str):
    from csv import reader
    
    sup, buy = 0, 0
    with open(data_file_name, 'r') as file:
        for op, val in reader(file):
            match op:
                case "supply":
                    sup += int(val)
                case "buy":
                    buy += int(val)
    
    with open(report_file_name, '+a') as report:
        report.write(
           f"supply,{sup}\n"
           f"buy,{buy}\n"
           f"result,{sup - buy}\n"
        )
        
        
create_report("apples.csv", "apples_report")
# def create_report(data_file_name: str, report_file_name: str):
#     from csv import reader
#     supply, buy = [], []
#     with open(data_file_name, 'r') as file:
#         for op, val in reader(file):
#             if op == "supply":
#                 supply.append(int(val))
#             if op == "buy":
#                 buy.append(int(val))
#     supply, buy = sum(supply), sum(buy)
#     with open(report_file_name, '+a') as report:
#         report.write(
#            f"supply,{supply}\n"
#            f"buy,{buy}\n"
#            f"result,{supply - buy}\n"
#         )
        

