from behinesazan.gas.station.software.model.gas.Gas import Gas




if __name__ == "__main__":
    g = Gas()
    g.calculate(250 * 6.89476, 273.15+8)
    print(g.T_h)
    pass