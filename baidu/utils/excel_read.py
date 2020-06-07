from openpyxl import load_workbook


class ParseExcel():
    def __int__(self, excel_path):
        self.wb = load_workbook(excel_Path)
        self.sheet = self.wb[data_sou]

    def getDataFromSheet(self):
        dataList = []
        for line in self.sheet:
            dataList.append(line[0].value)
            dataList.pop(0)

            return dataList

            # print(line)


if __name__ == '__main__':
    excel_Path = './../data_mange/test_data.xls'
    sheetName = 'data_sou'
    pe = ParseExcel(excel_Path, sheetName)
    print(pe.getDataFromSheet())
