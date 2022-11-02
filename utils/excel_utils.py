
import openpyxl
import os


class XlsxReader:

    @staticmethod
    def get_test_data(testcaseName):
        data = []
        filepath=os.path.join(os.path.abspath(os.curdir), 
            'resources','input_data.xlsx')
        book = openpyxl.load_workbook(filepath)
        sheet = book.active

        # loop every row
        for i in range(1, sheet.max_row+1):
            if sheet.cell(row=i, column=1).value == testcaseName:
                # loop through each column
                for j in range(2, sheet.max_column+1):
                    data.append(sheet.cell(row=i, column=j).value)
                break
        return data

    def get_test_data_based_on_sheet(sheet_name, test_case_name):
        data = []

        filepath=os.path.join(os.path.abspath(os.curdir), 
            'resources','input_data.xlsx')
        book = openpyxl.load_workbook(filepath)
        sheet = book[sheet_name]

        # loop every row
        for i in range(1, sheet.max_row+1):
            if sheet.cell(row=i, column=1).value == test_case_name:
                # loop through each column
                for j in range(2, sheet.max_column+1):
                    data.append(sheet.cell(row=i, column=j).value)
                break
        return data
        