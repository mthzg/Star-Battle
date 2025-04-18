import tkinter as tk

class Grid_UI:
    def __init__(self, board):
        self.board = board
        self.root = tk.Tk()
        self.root.title("Grille Star Battle")
        self.labels = {}
        
        # Frame principale
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)
        
        # Frame pour la grille
        self.grid_frame = tk.Frame(self.main_frame)
        self.grid_frame.pack()
        
        self.display_grid_interface()
        self.add_control_buttons()
        
    def get_region_color(self, region):
        colors = {
            0: "#FF9999",
            1: "#99FF99",
            2: "#9999FF",
            3: "#FFFF99",
            4: "#FF99FF",
            5: "#99FFFF",
            6: "#FFCC99",
            7: "#CCFF99",
            8: "#99CCFF",
            9: "#FF99CC"
        }
        return colors.get(region)
        
    def display_grid_interface(self):
        for i in range(self.board.n):
            for j in range(self.board.n):
                cell_region_id = self.board.grid[i][j]
                label = tk.Label(
                    self.grid_frame,
                    text="",
                    width=5,
                    height=2,
                    relief="solid",
                    bg=self.get_region_color(cell_region_id),
                    borderwidth=1
                )
                label.grid(row=i, column=j)
                self.labels[(i,j)] = label
                
    def add_control_buttons(self):
        btn_frame = tk.Frame(self.main_frame)
        btn_frame.pack(pady=10)
        
        tk.Button(
            btn_frame,
            text="Ajouter étoile régions",
            command=self.add_stars
        ).pack(side="left", padx=5)
        
        tk.Button(
            btn_frame,
            text="Ajouter étoile colonnes",
            command=self.add_stars
        ).pack(side="left", padx=5)

        # Bouton pour effacer
        tk.Button(
            btn_frame,
            text="Effacer tout",
            command=self.clear_all
        ).pack(side="left", padx=5)
        
        # Bouton pour quitter
        tk.Button(
            btn_frame,
            text="Quitter",
            command=self.kill
        ).pack(side="left", padx=5)
    
    def add_stars(self):
        self.set_cell(0, 0, "★")
    
    def clear_all(self):
        for i in range(self.board.n):
            for j in range(self.board.n):
                self.set_cell(i, j, "")
                
    def set_cell(self, row, col, text):
        if (row, col) in self.labels:
            self.labels[(row, col)].config(text=text)
            self.update_display()
    
    def update_display(self):
        self.root.update_idletasks()
        
    def show(self):
        self.root.mainloop()

    def kill(self):
        self.root.destroy()