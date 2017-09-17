lengte = int(input('Hoe lang ben jij?: '))
if lengte >= 120:
    def lang_genoeg(lengte):
        return print("Je bent lang genoeg voor deze attractie.")
else:
    def lang_genoeg(lengte):
        return print("Sorry je bent te klein.")
lang_genoeg(lengte)