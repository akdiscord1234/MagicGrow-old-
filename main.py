# setup
# import statements
import gooeypie as gp
from matplotlib import pyplot as plt
import pandas as pd

#start window setup
app = gp.GooeyPieApp("MagicGrow app")
app.width = 500
app.set_icon("hydroponics image.png")

# links
Link_weather = gp.Hyperlink(app, 'Weather in your area', 'https://weather.com/')
Link_expl = gp.Hyperlink(app, "What is hydroponics", "https://www.custommade.com/blog/introduction-to-hydroponics/")


# windows

# pH window
def pH_win(event):
    # setup
    subph = gp.Window(app, title="pH controls")
    subph.set_resizable(True)
    subph.set_size(width=300, height=300)
    subph.show()  # have to set width and height before

    # Chart
    def pHChart_win(event):
        # chart window setup
        subpHChart = gp.Window(subph, title="chart")
        subpHChart.set_size(width=200, height=200)
        subpHChart.show()

        # chart itself
        data = pd.read_csv('pH Chart.csv')

        plt.plot(data['jan'], data["6"], c="green", linewidth=10)

        plt.ylabel("pH level")
        plt.xlabel("month")

        plt.show()

    # widgets
    pH_label = gp.Number(subph, 0, 10)  # Use number widget here
    pHChart_btn = gp.Button(subph, "open chart", pHChart_win)
    pH_icon = gp.Image(subph, "pH_icon.jpg")
    # grid
    subph.set_grid(3, 1)
    subph.add(pH_icon, 1, 1, align="left")
    subph.add(pH_label, 2, 1, align="center")
    subph.add(pHChart_btn, 3, 1, align="center")


# Temperature window
def Temp_win(event):
    # setup
    subTemp = gp.Window(app, title="Temperature controls(°F)")
    subTemp.set_size(width=300, height=300)
    subTemp.show()

    # Chart
    def TempChart_win(event):
        # chart window setup
        subTempChart = gp.Window(subTemp, title="chart")
        subTempChart.set_size(width=200, height=200)
        subTempChart.show()

        # chart itself
        data = pd.read_csv('Temperature Chart.csv')

        plt.plot(data['jan'], data["50"], c="green", linewidth=10)

        plt.ylabel("temperature")
        plt.xlabel("month")

        plt.show()

    # widgets
    Temp_text = gp.Label(subTemp, "Temperature(°F)")
    Temp_label = gp.Number(subTemp, 0, 100)
    TempChart_btn = gp.Button(subTemp, "open chart", TempChart_win)
    Temp_icon = gp.Image(subTemp, "Temp_icon.jpg")
    # grid
    subTemp.set_grid(3, 2)
    subTemp.add(Temp_text, 1, 1, align="left")
    subTemp.add(Temp_icon, 1, 2, align="center")
    subTemp.add(Temp_label, 2, 1, align="left")
    subTemp.add(TempChart_btn, 3, 1, align="right")


# Ec
def Ec_win(event):
    # setup
    subEc = gp.Window(app, title="Ec controls")
    subEc.set_size(width=300, height=300)
    subEc.show()

    # Chart
    def EcChart_win(event):
        # chart window setup
        subEcChart = gp.Window(subEc, title="chart")
        subEcChart.set_size(width=200, height=200)
        subEcChart.show()

        # chart itself
        data = pd.read_csv('Ec Chart.csv')

        plt.plot(data['jan'], data["2.2"], c="green", linewidth=10)

        plt.ylabel("Ec level")
        plt.xlabel("month")

        plt.show()

    # widgets
    Ec_label = gp.Number(subEc, 0, 3)  # Use number widget here
    Ec_ex_label = gp.Label(subEc, "(EC means electrical conductivity, and the minerals and nutrients in the water\
    conduct electricity and therefore the EC level shows the Electrical conductivity.)")
    EcChart_btn = gp.Button(subEc, "open chart", EcChart_win)
    Ec_icon = gp.Image(subEc, "Ec_icon.jpg")
    # grid
    subEc.set_grid(4, 1)
    subEc.add(Ec_icon, 1, 1, align="left")
    subEc.add(Ec_label, 2, 1, align="center")
    subEc.add(EcChart_btn, 3, 1, align="center")
    subEc.add(Ec_ex_label, 4, 1, align="right")


# light window
def L_win(event):
    # setup
    subL = gp.Window(app, title="Light controls")
    subL.set_resizable(True)
    subL.set_size(width=350, height=300)
    subL.show()  # have to set width and height before

    # Chart

    def LChart_win(event):
        # chart window setup
        subLChart = gp.Window(subL, title="chart")
        subLChart.set_size(width=200, height=200)
        subLChart.show()

        # chart itself
        data = pd.read_csv('Light Chart.csv')

        plt.plot(data['jan'], data["10"], c="green", linewidth=10)

        plt.ylabel("Hours of light")
        plt.xlabel("month")
        plt.show()

    # widgets
    L_text = gp.Label(subL, "Light (# of hours of light in the day)")
    L_label = gp.Number(subL, 0, 24)
    LChart_btn = gp.Button(subL, "open chart", LChart_win)
    L_icon = gp.Image(subL, "Light_icon.png")
    # grid
    subL.set_grid(3, 2)
    subL.add(L_text, 1, 1, align="left")
    subL.add(L_icon, 1, 2, align="left")
    subL.add(L_label, 2, 1, align="center")
    subL.add(LChart_btn, 3, 1, align="center")


def Pump_win(event):
    # setup
    subP = gp.Window(app, title="Pump controls")
    subP.set_resizable(True)
    subP.set_size(width=500, height=150)
    subP.show()  # have to set width and height before
    # widgets
    # pump on/off dropdown
    onlist = ["ON", "OFF"]
    pump_drp = gp.Dropdown(subP, onlist)
    pump_drp.selected_index = 0
    pump_drp.width = 500

    # on alarm

    On_Inp = gp.Input(subP)
    On_Inp.text = "time for pump to start"
    On_Inp.justify = "left"
    On_Inp.width = 20

    # off alarmS
    Off_Inp = gp.Input(subP)
    Off_Inp.justify = "left"
    Off_Inp.width = 20
    Off_Inp.text = "time for pump to stop"

    # grid
    subP.set_grid(3, 1)
    subP.add(pump_drp, 1, 1, align="center")
    subP.add(On_Inp, 2, 1)
    subP.add(Off_Inp, 3, 1)


# main page buttons/images
# buttons
pH_btn = gp.Button(app, "pH controls", pH_win)
Temp_btn = gp.Button(app, "Temperature Controls", Temp_win)
Ec_btn = gp.Button(app, "Ec Controls", Ec_win)
L_btn = gp.Button(app, "Light controls", L_win)
Pump_btn = gp.Button(app, "Pump ON/OFF", Pump_win)
# images
Hydro_img_small = gp.Image(app, "hydroponics image small.jpg")
Small_Side_img = gp.Image(app, "Side_icon.png")

# grid
app.set_grid(7, 2)  # rows, column
app.add(Link_weather, 1, 1, align="left")
app.add(Hydro_img_small, 2, 2, align="left")
app.add(Link_expl, 2, 1, align="left")
app.add(pH_btn, 3, 1, align="center")
app.add(Temp_btn, 4, 1, align="center")
app.add(Ec_btn, 5, 1, align="center")
app.add(L_btn, 6, 1, align="center")
app.add(Pump_btn, 7, 1, align="center")
app.add(Small_Side_img, 7, 2, align="left")
app.run()
