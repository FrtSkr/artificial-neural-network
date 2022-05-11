import pandas as pd

class DataSet:
    def __init__(self):
        self.dataSet = pd.read_excel('./enerji-veri-seti.xls')
        self.dataArrX = []
        self.dataArrY = []
        self.minOfColumnsX = []
        self.maxOfColumnsX = []
        self.dataOrganizing()

    # Veri setimizdeki bağımsız değişkenler matris formuna getirildi ve bağımlı değişken değerleri vektörel olarak alındı
    def dataOrganizing(self):
        counter = 0
        self.dataArrX.clear()
        self.dataArrY.clear()
        while counter < len(self.dataSet):
            self.dataArrX.append(
                [self.dataSet.loc[counter, self.dataSet.columns[0]], self.dataSet.loc[counter, self.dataSet.columns[1]],
                 self.dataSet.loc[counter, self.dataSet.columns[2]],
                 self.dataSet.loc[counter, self.dataSet.columns[3]],
                 self.dataSet.loc[counter, self.dataSet.columns[4]], self.dataSet.loc[counter, self.dataSet.columns[5]],
                 self.dataSet.loc[counter, self.dataSet.columns[6]],
                 self.dataSet.loc[counter, self.dataSet.columns[7]]])
            self.dataArrY.append(self.dataSet.loc[counter, self.dataSet.columns[8]])
            counter += 1

    # Normalizasyon için kullanılacak olan herbir bağımsız değişkene ait minimum ve maksimum değer bulundu
    def minAndMaxValuesOfTheColumnsX(self, dataArrX):
        for i in range(len(dataArrX[0])):
            counter = 0
            columnMin = dataArrX[counter][i]
            columnMax = dataArrX[counter][i]
            while counter < len(dataArrX):
                if columnMin > dataArrX[counter][i]:
                    columnMin = dataArrX[counter][i]
                if columnMax < dataArrX[counter][i]:
                    columnMax = dataArrX[counter][i]
                counter += 1
            self.maxOfColumnsX.append(columnMax)
            self.minOfColumnsX.append(columnMin)
        return self.minOfColumnsX, self.maxOfColumnsX

    # Normalizasyon için kullanılacak olan herbir bağımlı değişkene ait minimum ve maksimum değer bulundu
    def minAndMaxValuesOfTheColumnsY(self, dataArrY):
        columnMinY = dataArrY[0]
        columnMaxY = dataArrY[0]
        for i in range(len(dataArrY)):
            if columnMaxY < dataArrY[i]:
                columnMaxY = dataArrY[i]
            if columnMinY > dataArrY[i]:
                columnMinY = dataArrY[i]
        return columnMinY, columnMaxY

    # Verilerimiz 0 - 1 aralığında normalize edilecek
    def normalizationMethod(self, x, xMin, xMax):
        return (x - xMin) / (xMax - xMin)

    # Bağımsız değişken veri seti normalize edildi
    def normalizedDataX(self):
        min, max = self.minAndMaxValuesOfTheColumnsX(self.dataArrX)
        for i in range(len(self.dataArrX)):
            for j in range(len(self.dataArrX[0])):
                normalize = self.normalizationMethod(self.dataArrX[i][j], min[j], max[j])
                self.dataArrX[i][j] = normalize
        return self.dataArrX

    # Bağımlı değişken veri seti normalize edildi
    def normalizedDataY(self):
        min, max = self.minAndMaxValuesOfTheColumnsY(self.dataArrY)
        for i in range(len(self.dataArrY)):
            normalize = self.normalizationMethod(self.dataArrY[i], min, max)
            self.dataArrY[i] = normalize
        return self.dataArrY