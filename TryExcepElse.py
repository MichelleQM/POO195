from tkinter import messagebox

class verification:
    def veri(self, user, password):
        try:
            if user == 'root' and password == 'root':
                return True
            else:
                return False
        except Exception as e:
            print(f"Error en la verificacion: {str(e)}")
            return False