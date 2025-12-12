# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    # Читаємо дані з файлу
    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
