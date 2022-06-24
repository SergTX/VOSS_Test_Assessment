@echo off



pytest -v -s -m "smoke or regression" --alluredir="C:\Users\serge\OneDrive\Desktop\TestAssesment_01_VOSS_QA\Reports\allureReports" --browser chrome

pytest -v -s -m "smoke or regression" --alluredir="C:\Users\serge\OneDrive\Desktop\TestAssesment_01_VOSS_QA\Reports\allureReports" --browser Firefox

pytest -v -s -m "smoke or regression" --alluredir="C:\Users\serge\OneDrive\Desktop\TestAssesment_01_VOSS_QA\Reports\allureReports" --browser Medge

pause