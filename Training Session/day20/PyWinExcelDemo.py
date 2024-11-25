import win32com.client

def CreateExcelWorkbook(filePath):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True

    workbook = excel.Workbooks.Add()

    sheet = workbook.Sheets(1)
    sheet.Cells(1,1).Value = "Priyanka's Sample Excel Workbook"
    sheet.Cells(2,1).Value = "This is a demo auto generated excel"

    workbook.SaveAs(filePath)
    excel.Quit()

CreateExcelWorkbook(r"C:\Users\Administrator\Documents\UST Training\Python-Training\Training Session\day20\ExcelSample.xlsx")
