import time

class Algo:
    def __init__(self, interface):
        self.interface = interface
        self.n = self.interface.board.n
        self.k = 2  # Nombre d'étoiles par ligne/colonne/région
        

    def count_stars_on_row(self, row)-> int:
        counter = 0
        for i in range(self.n):
            if self.interface.get_cell_text(row, i) == "★":
                counter += 1
        return counter

    def count_stars_on_column(self, col) -> int:
        counter = 0
        for i in range(self.n):
            if self.interface.get_cell_text(i, col) == "★":
                counter += 1
        return counter
    
    def count_stars_in_regions(self, region_id) -> int:
        counter = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.interface.board.grid[i][j] == region_id:
                    if self.interface.get_cell_text(i, j) == "★":
                        counter += 1
        return counter
    

    def place_blocked_cells_grid(self):
        for row in range(self.n):
            for col in range(self.n):
                region_id = self.interface.board.grid[row][col]

                #regions
                if self.count_stars_in_regions(region_id) == 2:
                    self.place_blocked_cell_on_region(region_id)

                #lignes
                if self.count_stars_on_row(row) == 2:
                    self.place_blocked_cell_on_row(row)

                #colonnes
                if self.count_stars_on_column(col) == 2:
                    self.place_blocked_cell_on_column(col)

                #adjacent
                if self.interface.get_cell_text(row, col) == "★":
                    self.place_blocked_cell(row, col)


    def clear_all_blocked_cells(self):
        for row in range(self.n):
            for col in range(self.n):
                if self.interface.get_cell_text(row, col) == "X":
                    self.interface.set_cell(row, col, "")

    def manage_blocked_cell(self):
        self.clear_all_blocked_cells()
        self.place_blocked_cells_grid()




    

    def is_adjacent(self, row, col) -> bool:
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),          (0,1),
                      (1,-1),  (1,0), (1,1)]
        
        for d_r, d_c in directions:
            r, c = row + d_r, col + d_c
            if 0 <= r < self.n and 0 <= c < self.n:
                if self.interface.get_cell_text(r, c) == "★":
                    return True
        return False
    

    def place_blocked_cell(self, row, col) -> None:
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),          (0,1),
                      (1,-1),  (1,0), (1,1)]
        for d_r, d_c in directions:
            r, c = row + d_r, col + d_c
            if 0 <= r < self.n and 0 <= c < self.n:
                self.interface.set_cell(r, c, "X")

    def remove_blocked_cell(self, row, col) -> None:
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),          (0,1),
                      (1,-1),  (1,0), (1,1)]
        for d_r, d_c in directions:
            r, c = row + d_r, col + d_c
            if 0 <= r < self.n and 0 <= c < self.n:
                self.interface.set_cell(r, c, "")


    def place_blocked_cell_on_column(self, col) -> None:
        for i in range(self.n):
            if self.interface.get_cell_text(i, col) == "":
                self.interface.set_cell(i, col, "X")

    def remove_blocked_cell_on_column(self, col) -> None:
        for i in range(self.n):
            if self.interface.get_cell_text(i, col) == "":
                self.interface.set_cell(i, col, "")


    def place_blocked_cell_on_row(self, row) -> None:
        for i in range(self.n):
            if self.interface.get_cell_text(row, i) == "":
                self.interface.set_cell(row, i, "X")

    def remove_blocked_cell_on_row(self, row) -> None:
        for i in range(self.n):
            if self.interface.get_cell_text(row, i) == "":
                self.interface.set_cell(row, i, "")


    def place_blocked_cell_on_region(self, region_id) -> None:
        for row in range(self.n):
            for col in range(self.n):
                if (self.interface.board.grid[row][col] == region_id and 
                    self.interface.get_cell_text(row, col) == ""):
                    self.interface.set_cell(row, col, "X")

    def remove_blocked_cell_on_region(self, region_id) -> None:
        for row in range(self.n):
            for col in range(self.n):
                if (self.interface.board.grid[row][col] == region_id and 
                    self.interface.get_cell_text(row, col) == "X"):
                    self.interface.set_cell(row, col, "")



    def is_valid(self, row, col) -> bool:
        region_id = self.interface.board.grid[row][col]
        if (self.interface.get_cell_text(row, col)) != "★":
            if (self.count_stars_on_row(row) < 2):
                if (self.count_stars_on_column(col) < 2):
                    if (self.count_stars_in_regions(region_id) < 2):
                        if (not self.is_adjacent(row, col)):
                            return True
        return False 
    
        
    def is_solution_valid(self) -> bool:
        for row in range(self.n):
            if self.count_stars_on_row(row) != 2:
                return False

        for col in range(self.n):
            if self.count_stars_on_column(col) != 2:
                return False
        
        regions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for region in regions:
            if self.count_stars_in_regions(region) != 2:
                return False

        
        return True
    
    def check_all_regions_still_valid(self, region_order, region_index):
        for region in region_order[region_index+1:]:
            valid_cells = 0
            for row in range(self.n):
                for col in range(self.n):
                    #if not (self.interface.board.grid[row][col] == region):
                        #print("1 pour :", col, ",", row)
                    #if not (self.interface.get_cell_text(row, col) == ""):
                        #print("2 pour :", col, ",", row)
                    #if not (self.is_valid(row, col)):
                        #print("3 pour :", col, ",", row)
                    if (self.interface.board.grid[row][col] == region and self.interface.get_cell_text(row, col) == "" and self.is_valid(row, col)):
                        valid_cells += 1
            if valid_cells < self.k:
                return False
        return True



    def solve_backtracking_cols(self, col=0, stars_placed=0, start_row=0):
        """Backtracking en parcourant les colonnes"""
        # Vérifier si la solution actuelle est complète et valide
        if self.is_solution_valid():
            return True

        # Si on a placé k étoiles dans cette colonne, passer à la suivante
        if stars_placed == self.k:
            return self.solve_backtracking_cols(col + 1, 0, 0)

        # Si on a parcouru toutes les colonnes
        if col >= self.n:
            return False

        # Essayer de placer une étoile dans cette colonne
        for row in range(start_row, self.n):
            if self.is_valid(row, col):
                # Placer l'étoile
                self.interface.set_cell(row, col, "★")
                

                # Explorer récursivement
                if self.solve_backtracking_cols(col, stars_placed + 1, row + 1):
                    return True

                # Backtrack - enlever l'étoile
                self.interface.set_cell(row, col, "")

        return False
    
    #def solve_forward_checking_cols(self, col=0, stars_placed=0, start_row=0):
    #    """Your forward checking implementation with column-wise traversal"""
    #    # Check if current solution is complete and valid
    #    if self.is_solution_valid():
    #        return True
    #    # If we've placed k stars in this column, move to next column
    #    if stars_placed == self.k:
    #        self.place_blocked_cell_on_column(col)  # Block remaining cells in column
    #        result = self.solve_forward_checking_cols(col + 1, 0, 0)
    #        self.remove_blocked_cell_on_column(col)  # Unblock when backtracking
    #        return result
    #
    #    # If we've processed all columns
    #    if col >= self.n:
    #        return False
    #
    #    # Try to place a star in this column
    #    for row in range(start_row, self.n):
    #        if self.is_valid(row, col):
    #            # Place the star and block adjacent cells
    #            self.interface.set_cell(row, col, "★")
    #            self.place_blocked_cell(row, col)
    #
    #            # Recursive exploration
    #            if self.solve_forward_checking_cols(col, stars_placed + 1, row + 1):
    #                return True
    #
    #            # Backtrack: remove star and unblock adjacent cells
    #            self.remove_blocked_cell(row, col)
    #            self.interface.set_cell(row, col, "")
    #
    #    return False

    


    def solve_forward_checking_cols(self, col=0, stars_placed=0, start_row=0):
        """Your forward checking implementation with column-wise traversal"""

        self.manage_blocked_cell()
        #time.sleep(1)


        # Check if current solution is complete and valid
        if self.is_solution_valid():
            return True
        # If we've placed k stars in this column, move to next column
        if stars_placed == self.k:
            result = self.solve_forward_checking_cols(col + 1, 0, 0)
            return result
    
        # If we've processed all columns
        if col >= self.n:
            return False
    
        # Try to place a star in this column
        for row in range(start_row, self.n):
            if self.is_valid(row, col):
                # Place the star and block adjacent cells
                self.interface.set_cell(row, col, "★")
    
                # Recursive exploration
                if self.solve_forward_checking_cols(col, stars_placed + 1, row + 1):
                    return True
    
                # Backtrack: remove star and unblock adjacent cells
                self.interface.set_cell(row, col, "")
    
        return False



    def solve_backtracking_regions(self, region_order=None, star_index=0, region_index=0):
        """Backtracking using regions as domains, processing smallest regions first"""
        #time.sleep(2)
        # Initialize region order by size (smallest first)
        if region_order is None:
            regions = {}
            for row in range(self.n):
                for col in range(self.n):
                    region_id = self.interface.board.grid[row][col]
                    regions[region_id] = regions.get(region_id, 0) + 1

            # Sort regions by size (smallest first), then by region_id for consistency
            region_order = sorted(regions.keys(), key=lambda x: (regions[x], x))


            return self.solve_backtracking_regions(region_order, 0, 0)

        # Check if solution is complete
        if self.is_solution_valid():
            return True

        # If we've processed all regions
        if region_index >= len(region_order):
            return False

        current_region = region_order[region_index]

        # Get all empty cells in this region
        region_cells = []
        for row in range(self.n):
            for col in range(self.n):
                if (self.interface.board.grid[row][col] == current_region and 
                    self.interface.get_cell_text(row, col) == ""):
                    region_cells.append((row, col))

        # Try placing stars in this region's cells
        for i in range(star_index, len(region_cells)):
            row, col = region_cells[i]

            if self.is_valid(row, col):
                self.interface.set_cell(row, col, "★")

                # Recursive call - try next star in same region or move to next region
                next_star = star_index + 1
                next_region = region_index + (1 if next_star >= self.k else 0)
                next_star = 0 if next_star >= self.k else next_star

                if self.solve_backtracking_regions(region_order, next_star, next_region):
                    return True

                self.interface.set_cell(row, col, "")

        return False
    

    def solve_forward_checking_regions(self, region_order=None, stars_placed=0, region_index=0):
        """Forward checking with regions as domains (smallest regions first)"""
    
        self.manage_blocked_cell()
        #time.sleep(1)
        # Initialize region order by size (smallest first)
        if region_order is None:
            regions = {}
            for row in range(self.n):
                for col in range(self.n):
                    region_id = self.interface.board.grid[row][col]
                    regions[region_id] = regions.get(region_id, 0) + 1
            
            # Sort regions by size (smallest first), then by region_id
            region_order = sorted(regions.keys(), key=lambda x: (regions[x], x))
            return self.solve_forward_checking_regions(region_order, 0, 0)
    
        # Check if solution is complete
        if self.is_solution_valid():
            return True
    
        # If we've placed k stars in this region
        if stars_placed == self.k:
            # Block remaining cells in this region
            result = self.solve_forward_checking_regions(region_order, 0, region_index + 1)
            # Unblock when backtracking
            return result
    
        # If we've processed all regions
        if region_index >= len(region_order):
            return False
    
        current_region = region_order[region_index]
        
        # Get all valid empty cells in this region
        region_cells = []
        for row in range(self.n):
            for col in range(self.n):
                if (self.interface.board.grid[row][col] == current_region and
                    self.is_valid(row, col)):
                    region_cells.append((row, col))
    
        # Try placing stars in this region's cells
        for row, col in region_cells:
            # Place star and block adjacent cells
            self.interface.set_cell(row, col, "★")
            
            # Recursive call - try next star in same region
            if self.solve_forward_checking_regions(region_order, stars_placed + 1, region_index):
                return True
                
            # Backtrack - remove star and unblock adjacent cells
            self.interface.set_cell(row, col, "")
    
        return False
    

    #def solve_forward_checking_regions(self, region_order=None, stars_placed=0, region_index=0):
    #    """Forward checking with regions as domains (smallest regions first)"""
    #    #time.sleep(2)
    #    # Initialize region order by size (smallest first)
    #    if region_order is None:
    #        regions = {}
    #        for row in range(self.n):
    #            for col in range(self.n):
    #                region_id = self.interface.board.grid[row][col]
    #                regions[region_id] = regions.get(region_id, 0) + 1
    #        
    #        # Sort regions by size (smallest first), then by region_id
    #        region_order = sorted(regions.keys(), key=lambda x: (regions[x], x))
    #        return self.solve_forward_checking_regions(region_order, 0, 0)
    #
    #    # Check if solution is complete
    #    if self.is_solution_valid():
    #        return True
    #
    #    # If we've placed k stars in this region
    #    if stars_placed == self.k:
    #        # Block remaining cells in this region
    #        self.place_blocked_cell_on_region(region_order[region_index])
    #        result = self.solve_forward_checking_regions(region_order, 0, region_index + 1)
    #        # Unblock when backtracking
    #        self.remove_blocked_cell_on_region(region_order[region_index])
    #        return result
    #
    #    # If we've processed all regions
    #    if region_index >= len(region_order):
    #        return False
    #
    #    current_region = region_order[region_index]
    #    
    #    # Get all valid empty cells in this region
    #    region_cells = []
    #    for row in range(self.n):
    #        for col in range(self.n):
    #            if (self.interface.board.grid[row][col] == current_region and
    #                self.interface.get_cell_text(row, col) == "" and
    #                self.is_valid(row, col)):
    #                region_cells.append((row, col))
    #
    #    # Try placing stars in this region's cells
    #    for row, col in region_cells:
    #        # Place star and block adjacent cells
    #        self.interface.set_cell(row, col, "★")
    #        self.place_blocked_cell(row, col)
    #        
    #        # Recursive call - try next star in same region
    #        if self.solve_forward_checking_regions(region_order, stars_placed + 1, region_index):
    #            return True
    #            
    #        # Backtrack - remove star and unblock adjacent cells
    #        self.remove_blocked_cell(row, col)
    #        self.interface.set_cell(row, col, "")
    #
    #    return False


    def solve_forward_checking_MRV_regions(self, region_order=None, stars_placed=0, region_index=0):
        """Forward checking with regions as domains + dynamic MRV (smallest region first at each step)"""

        # Initialize region order dynamically at the first call
        if region_order is None:
            region_order = []

        # Check if solution is complete
        if self.is_solution_valid():
            return True

        # If we've processed all current regions, pick the next region dynamically using MRV
        if region_index >= len(region_order):
            # Map region_id to list of valid cells
            regions = {}
            for row in range(self.n):
                for col in range(self.n):
                    region_id = self.interface.board.grid[row][col]
                    if region_id not in region_order:
                        if region_id not in regions:
                            regions[region_id] = []
                        if (self.interface.get_cell_text(row, col) == "" and
                            self.is_valid(row, col)):
                            regions[region_id].append((row, col))

            if not regions:
                return False  # No regions left but solution incomplete

            # MRV: select region with fewest valid cells
            next_region = min(regions.keys(), key=lambda r: len(regions[r]))
            region_order.append(next_region)
            return self.solve_forward_checking_MRV_regions(region_order, 0, region_index)

        current_region = region_order[region_index]

        # If we've placed k stars in this region
        if stars_placed == self.k:
            self.place_blocked_cell_on_region(current_region)
            result = self.solve_forward_checking_MRV_regions(region_order, 0, region_index + 1)
            self.remove_blocked_cell_on_region(current_region)
            return result

        # Get all valid empty cells in this region
        region_cells = []
        for row in range(self.n):
            for col in range(self.n):
                if (self.interface.board.grid[row][col] == current_region and
                    self.interface.get_cell_text(row, col) == "" and
                    self.is_valid(row, col)):
                    region_cells.append((row, col))

        # Try placing stars in this region's cells
        for row, col in region_cells:
            self.interface.set_cell(row, col, "★")
            self.place_blocked_cell(row, col)

            if self.solve_forward_checking_MRV_regions(region_order, stars_placed + 1, region_index):
                return True

            # Backtrack
            self.remove_blocked_cell(row, col)
            self.interface.set_cell(row, col, "")

        return False
    

    def solve_forward_checking_MRV_cols(self, col=0, stars_placed=0, start_row=0, cols_order=None):
        """Column-wise forward checking with MRV in single method"""
        # Initialize column order by MRV (only at first call)
        if cols_order is None:
            # Create initial column order based on remaining valid placements
            col_constraints = []
            for c in range(self.n):
                valid_cells = 0
                for r in range(self.n):
                    if (self.interface.get_cell_text(r, c) == "" and 
                        self.is_valid(r, c)):
                        valid_cells += 1
                col_constraints.append((valid_cells, c))
            # Sort by number of valid placements, then original column order
            cols_order = [c for (val, c) in sorted(col_constraints)]
            return self.solve_forward_checking_MRV_cols(0, 0, 0, cols_order)

        # Check if solution is complete
        if self.is_solution_valid():
            return True

        # If we've placed k stars in this column, move to next MRV column
        if stars_placed == self.k:
            self.place_blocked_cell_on_column(cols_order[col])
            result = self.solve_forward_checking_MRV_cols(col + 1, 0, 0, cols_order)
            self.remove_blocked_cell_on_column(cols_order[col])
            return result

        # If we've processed all columns
        if col >= len(cols_order):
            return False

        current_col = cols_order[col]

        # Try to place a star in this column
        for row in range(start_row, self.n):
            if self.is_valid(row, current_col):
                # Place star and block adjacent cells
                self.interface.set_cell(row, current_col, "★")
                self.place_blocked_cell(row, current_col)

                # Recursive call
                if self.solve_forward_checking_MRV_cols(col, stars_placed + 1, row + 1, cols_order):
                    return True

                # Backtrack
                self.remove_blocked_cell(row, current_col)
                self.interface.set_cell(row, current_col, "")

        return False





    def solve(self, choice):
        self.interface.clear_all()

        if (choice == 1):
            if self.solve_backtracking_cols(start_row=6):
                print("solve_backtracking_cols Solution trouvée et affichée")
                return True
            else:
                print("solve_backtracking_cols Aucune solution trouvée")
                return False
        elif (choice == 2):
            if self.solve_forward_checking_cols(start_row=6):
                print("solve_forward_checking_cols Solution trouvée et affichée")
                return True
            else:
                print("solve_forward_checking_cols Aucune solution trouvée")
                return False
        elif (choice == 3):
            if self.solve_backtracking_regions():
                print("solve_backtracking_regions Solution trouvée et affichée")
                return True
            else:
                print("solve_backtracking_regions Aucune solution trouvée")
                return False
        elif (choice == 4):
            if self.solve_forward_checking_regions():
                print("solve_forward_checking_regions Solution trouvée et affichée")
                return True
            else:
                print("solve_forward_checking_regions Aucune solution trouvée")
                return False
        elif (choice == 5):
            if self.solve_forward_checking_MRV_cols():
                print("solve_forward_checking_MRV_cols Solution trouvée et affichée")
                return True
            else:
                print("solve_forward_checking_MRV_cols Aucune solution trouvée")
                return False            
        elif (choice == 6):
            if self.solve_forward_checking_MRV_regions():
                print("solve_forward_checking_MRV_regions Solution trouvée et affichée")
                return True
            else:
                print("solve_forward_checking_MRV_regions Aucune solution trouvée")
                return False