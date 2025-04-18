class Board:
    def __init__(self, n):
        self.n = n
        self.grid = self.create_grid()

    def create_grid(self):
        return [[0,0,0,0,1,1,1,2,3,3],
                [0,0,4,0,1,2,2,2,3,3],
                [4,0,4,0,2,2,2,2,2,3],
                [4,0,4,0,2,2,6,6,2,3],
                [4,4,4,4,5,6,6,6,6,7],
                [4,4,8,5,5,5,5,5,6,7],
                [9,9,8,8,8,8,5,6,6,7],
                [9,9,8,5,5,5,5,6,6,7],
                [9,8,8,5,5,5,7,6,6,7],
                [8,8,8,5,5,5,7,7,7,7]]
        #grid = []
        #for i in range(self.n):
        #    row = []
        #    for j in range(self.n):
        #        row.append(0)
        #    grid.append(row)
        #return grid
    
    def display_grid(self):
        print("\n"+"    ", end="")
        for i in range (self.n):
            print(f" {i+1:2}", end="")
        print()
        print("   -" + "---" * self.n)
        row_number = 1
        for row in self.grid:
            formated_row = " ".join(f"{cell:2}" for cell in row)
            print(f"{row_number:2} | {formated_row}" )
            row_number += 1
        print("\n")