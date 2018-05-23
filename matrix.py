
def checkMatrix(func):
    def check(matrix1, matrix2):
        if len(matrix1.matrix) != len(matrix2.matrix):
            raise ValueError
    
        elif len(matrix1.matrix[0]) != len(matrix2.matrix[0]):
            raise ValueError
        else:
            func(matrix1, matrix2)
    return check
        


class Matrix:
    def __init__(self, Rows, Columns):
        print("matrix")
        self.rows = Rows
        self.cols = Columns
        self.matrix = []
        
        for i in range(self.rows):
            col = self.cols * [0]
            self.matrix.append(col)

    @checkMatrix
    def add(self, matrix2):
        tempMatrix = []
        for i in range(len(self.matrix)):
            tempMatrix.append([])
            for j in range(len(self.matrix[1])):
                tempMatrix[-1].append(self.matrix[i][j] + matrix2.matrix[i][j])
        self.matrix = tempMatrix
        return tempMatrix
            
    @checkMatrix
    def sub(self,matrix2):
        tempMatrix = []
        for i in range(len(self.matrix)):
            tempMatrix.append([])
            for j in range(len(self.matrix[1])):
                tempMatrix[-1].append(self.matrix[i][j] - matrix2.matrix[i][j])
        self.matrix = tempMatrix
        return tempMatrix
    
