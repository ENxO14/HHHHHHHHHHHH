import pandas as pd

Timeseries = pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='Timeseries Plot')
RawData = pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='Raw Data')
ModelError = pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='Model Error')
PieChartContriubtion = pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='Pie Chart Contriubtion')
StackedPlotContribution = pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='Stacked Plot Contribution')
ROASDisplay= pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='ROAS - Display')
ROASFacebook= pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='ROAS - Facebook')
ROASGooglePLA= pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='ROAS - Google PLA')
ROASGoogleSearch= pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='ROAS - Google Search')
ROASMicrosoft = pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='ROAS - Microsoft')
MediaSpendAverages = pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='Media Spend Averages')
Overview = pd.read_excel ("/content/Dashboard Data.xlsx",sheet_name='Overview')