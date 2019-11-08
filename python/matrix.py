class matrix:
    def __init__(self, vals):
        self.vals = vals
        self.shape = (len(vals), len(vals[0]))
        
    def __str__(self):
        temp = '['
        for i in range(self.shape[0] - 1):
            temp += str(self.vals[i])
            temp += ', '
        temp += str(self.vals[-1])
        temp += ']'
        return temp
    
    def __repr__(self):
        temp = '['
        for i in range(self.shape[0] - 1):
            temp += str(self.vals[i])
            temp += ', '
        temp += str(self.vals[-1])
        temp += ']'
        return temp
    
    def __add__(self, rhs):
        if(self.shape != rhs.shape):
            raise
        c = []
        for i in range(len(self.shape[0])):
            c.append([])
            for j in range(len(self.vals[1])):
                c[i].append(self.vals[i][j] + rhs.vals[i][j])
        return matrix(c)
    
    def __add__(self, rhs):
        if(self.shape != rhs.shape):
            raise
        c = []
        for i in range(len(self.shape[0])):
            c.append([])
            for j in range(len(self.vals[1])):
                c[i].append(self.vals[i][j] - rhs.vals[i][j])
        return matrix(c)
    
    def __mul__(self, rhs):
        c = []
        for i in range(self.shape[0]):
            c.append([])
            for j in range(rhs.shape[1]):
                c[i].append(0)                
                for k in range(self.shape[1]):
                    c[i][j] += self.vals[i][k] * rhs.vals[k][j]
        return matrix(c)
    
    def Transpose(self):
        c = []
        for i in range(self.shape[0]):
            c.append([x[i] for x in self.vals])
        return matrix(c)





