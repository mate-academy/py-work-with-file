class MarketReport:
    def __init__(self, data_file_name: str, report_file_name: str) -> None:
        self.data_file_name = data_file_name
        self.report_file_name = report_file_name
        self.supply_total = 0
        self.buy_total = 0

    def read_data(self) -> None:
        with open(self.data_file_name, "r") as data_file:
            for line in data_file:
                line = line.strip()
                if not line:
                    continue
                operation, amount = line.split(",")
                amount = int(amount)
                if operation == "supply":
                    self.supply_total += amount
                elif operation == "buy":
                    self.buy_total += amount

    def calculate_result(self) -> int:
        return self.supply_total - self.buy_total

    def write_report(self) -> None:
        result = self.calculate_result()
        with open(self.report_file_name, "w") as report_file:
            report_file.write(f"supply,{self.supply_total}\n")
            report_file.write(f"buy,{self.buy_total}\n")
            report_file.write(f"result,{result}\n")

    def create_report(self) -> None:
        self.read_data()
        self.write_report()


def create_report(data_file_name: str, report_file_name: str) -> None:
    report = MarketReport(data_file_name, report_file_name)
    report.create_report()
