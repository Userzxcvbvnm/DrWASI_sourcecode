class Function:
    def __init__(self, nfd = False):
        self.name = ""
        self.par = set()
        self.functionality = ""
        self.posix = ""
        self.needfd = nfd
    
    def print(self):
        print(self.get())
    
    def get(self):
        c =  (f"Function name: {self.name}\nFunction pars: ")
        for p in self.par:
            c += p
            c += " "
        c += f"\nFunctionality: {self.functionality}\n"
        if self.posix != "":
            c += f"POSIX func: {self.posix}\n"
        c += f"Need fd: {self.needfd}\n\n"
        return c
    


class WASIModel:
    def __init__(self):
        self.par = set()
        self.func = []

    def print(self):
        print(self.get())
    
    def get(self):
        c = f"Parameter number: {len(self.par)}\nFunction number: {len(self.func)}\n\n"
        c +=  (f"Parameters:= \n")
        for p in self.par:
            c += p
            c += " "
        c += "\n"

        c +=  (f"\n\n")
        for f in self.func:
            c += f.get()
        
        return c