class Algo:
    def __init__(self, interface):
        self.interface = interface
        
    def add_stars_regions(self):
        #for i in range(self.interface.board.n):
        #    for j in range(self.interface.board.n):
        #        if self.interface.get_cell_text(i, j) == "":
        #            self.interface.set_cell(i, j, "★")
        self.is_valid(0,0)

    def add_stars_columns(self):
        for j in range(self.interface.board.n):
            for i in range(self.interface.board.n):
                if self.interface.get_cell_text(i, j) == "":
                    self.interface.set_cell(i, j, "★")


    def count_stars_on_row(self, row)-> int:
        counter = 0
        for i in range(self.interface.board.n):
            if self.interface.get_cell_text(row, i) == "★":
                counter += 1
        print(f"stars on row = {row} = {counter}") #debug
        return counter

    def count_stars_on_column(self, col) -> int:
        counter = 0
        for i in range(self.interface.board.n):
            if self.interface.get_cell_text(i, col) == "★":
                counter += 1
        print(f"stars on col = {col} = {counter}") #debug
        return counter
    
    def count_stars_in_regions(self, region_id) -> int:
        counter = 0
        for i in range(self.interface.board.n):
            for j in range(self.interface.board.n):
                if self.interface.board.grid[i][j] == region_id:
                    if self.interface.get_cell_text(i, j) == "★":
                        counter += 1
        print(f"stars in region {region_id} = {counter}")
        return counter
    

    def is_adjacent(self, row, col) -> bool:
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),          (0,1),
                      (1,-1),  (1,0), (1,1)]
        
        for d_r, d_c in directions:
            r, c = row + d_r, col + d_c
            if 0 <= r < self.interface.board.n and 0 <= c < self.interface.board.n:
                if self.interface.get_cell_text(r, c) == "★":
                    return True
        return False
    

    def is_valid(self, row, col) -> bool:
        region_id = self.interface.board.grid[row][col]
        if (self.interface.get_cell_text(row, col)) == "":
            if (self.count_stars_on_row(row) < 2):
                if (self.count_stars_on_column(col) < 2):
                    if (self.count_stars_in_regions(region_id) < 2):
                        if (not self.is_adjacent(row, col)):
                            print("la case est valide")
                            return True
        print("VOUS NE PASSEREZ PAS !!!")
        return False 
        
        
        
        

    