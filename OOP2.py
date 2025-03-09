class Avto:
    def __init__ (self, model, rang, narh, kilometr):
        self.model=model
        self.rang=rang
        self.narh=narh
        self.kilometr=0
    def get_info(self):
        return f"{self.rang} rangli, {self.kilometr} km yurgan {self.model} nomli avtomabilimiz narhi {self.narh}"
    def set_update_km(self,km):
        self.kilometr=km
avtomabil1=Avto("malibu", "qora", "25000", 20000)
print(avtomabil1.model)  
print(avtomabil1.get_info())
avtomabil1.set_update_km(15000)
print(avtomabil1.get_info())
print(dir(str))