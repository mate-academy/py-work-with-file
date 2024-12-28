import csv

def create_report(data_file_name: str, report_file_name: str):
    supply_total = 0
    buy_total = 0
    
    file = open(data_file_name, mode='r')
    reader = csv.reader(file)
    
    next(reader, None)
    
    for row in reader:
        if row:
            operation, amount = row
            amount = int(amount) 
            
            if operation == 'supply':
                supply_total += amount
            elif operation == 'buy':
                buy_total += amount
    
    result = supply_total - buy_total
    
    file.close()
    
    file = open(report_file_name, mode='w', newline='')
    writer = csv.writer(file)
    
    writer.writerow(['supply', supply_total])
    writer.writerow(['buy', buy_total])
    writer.writerow(['result', result])
    
    file.close()
