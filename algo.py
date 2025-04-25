class Algo:
    def __init__(self, interface):
        self.interface = interface
        

    def count_stars_on_row(self, row)-> int:
        counter = 0
        for i in range(self.interface.board.n):
            if self.interface.get_cell_text(row, i) == "★":
                counter += 1
        return counter

    def count_stars_on_column(self, col) -> int:
        counter = 0
        for i in range(self.interface.board.n):
            if self.interface.get_cell_text(i, col) == "★":
                counter += 1
        return counter
    
    def count_stars_in_regions(self, region_id) -> int:
        counter = 0
        for i in range(self.interface.board.n):
            for j in range(self.interface.board.n):
                if self.interface.board.grid[i][j] == region_id:
                    if self.interface.get_cell_text(i, j) == "★":
                        counter += 1
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
                            return True
        return False 
    

    def backtracking_columns(self, start_row=6) -> None:
        if start_row <= self.interface.board.n:
            for col in range(self.interface.board.n):
                start = start_row if col == 0 else 0
                for row in range(start, self.interface.board.n):
                    if (self.is_valid(row, col)):
                        self.interface.set_cell(row, col, "★")
            if not self.is_solution_valid():
                print("not valid")
            else:
                print("solution found")
            #    self.interface.clear_all()
            #    self.backtracking_columns(start_row + 1)
        
    def is_solution_valid(self) -> bool:
        for row in range(self.interface.board.n):
            if self.count_stars_on_row(row) != 2:
                return False

        for col in range(self.interface.board.n):
            if self.count_stars_on_column(col) != 2:
                return False
        
        regions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for region in regions:
            if self.count_stars_in_regions(region) != 2:
                return False

        
        return True
    

    