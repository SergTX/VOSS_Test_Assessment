@echo off


pytest -v -s -m "smoke or regression" --alluredir="C:\Users\serge\OneDrive\Desktop\VOSS_Test_Assessment\Reports\allureReports" --browser chrome

pytest -v -s -m "smoke or regression" --alluredir="C:\Users\serge\OneDrive\Desktop\VOSS_Test_Assessment\Reports\allureReports" --browser Firefox

pytest -v -s -m "smoke or regression" --alluredir="C:\Users\serge\OneDrive\Desktop\VOSS_Test_Assessment\Reports\allureReports" --browser Medge

pause