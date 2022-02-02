import pytest

from app.main import create_report


@pytest.mark.parametrize(
    "data_file_name,report_file_name,expected_report",
    [
        (
            "apples.csv", "apples_report.csv", "supply,188\nbuy,115\nresult,73\n",
        ),
        (
            "bananas.csv", "bananas_report.csv", "supply,491\nbuy,293\nresult,198\n",
        ),
        (
            "grapes.csv", "grapes_report.csv", "supply,352\nbuy,352\nresult,0\n",
        ),
        (
            "oranges.csv", "oranges_report.csv", "supply,295\nbuy,154\nresult,141\n",
        ),
    ]
)
def test_create_report(data_file_name, report_file_name, expected_report):
    create_report(data_file_name, report_file_name)
    with open(report_file_name, "r") as report_file:
        assert report_file.read() == expected_report
