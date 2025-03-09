class Fan:
    def __init__ (self, fan_nomi, fan_davomiyligi, fan_ustozi):
        self.fan_nomi=fan_nomi
        self.fan_davomiyligi=fan_davomiyligi
        self.fan_ustozi=fan_ustozi
        self.fanlar=[]
    def get_info(self):
        info=f"{self.fan_nomi} fani davomiyligi {self.fan_davomiyligi}, "
        info+=f"fan ustozi {self.fan_ustozi}"
        return info
    def fanga_yozil(self, fan):
        self.fanlar.append(fan)
class Ustoz(Fan):
    def __init__(self, fan_nomi, fan_ustozi, daraja):
        super().__init__(fan_nomi, fan_ustozi)
        self.daraja=daraja

matem=Ustoz("matematika", "Ahmedov.I", "professor")
adab=Fan("adabiyot", "12 oy", "Yigitaliyev.Y")
adab.fanga_yozil(adab)


print(adab.fan_ustozi)
print(matem.get_info())
print(adab.get_info())