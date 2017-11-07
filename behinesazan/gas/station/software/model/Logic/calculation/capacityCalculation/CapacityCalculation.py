

class CapacityCalculation:

    def __init__(self):
        pass

    def gasConsumptionCal(self, Pin, Tin, Pout, Tout, g, HHV, debi):
        g.calculate(Pin, Tin)
        H1 = g.H
        g.calculate(Pout, Tout)
        H2 = g.H
        gasConsumption = self.capacityCal(Pin,
                                                   Tin,
                                                   g,
                                                   H1,
                                                   H2,
                                                   HHV,
                                                   debi)
        return gasConsumption

    def capacityCal(self, P, T, g, H1, H2, HHV, Q_standard):
        g.calculate(g.p_theta, g.T_theta)
        P2 = g.P
        Z2 = g.Z
        T2 = g.T
        Dstd = g.D # kg/m^3
        g.calculate(P, T)
        P1 = g.P
        Z1 = g.Z
        T1 = g.T


        C = (P2 * Z1 * T1) / (P1 * Z2 * T2)
        # change Q standard to debi in pipeline with input pressure
        Qdot = (Q_standard / 3600) * C
        # calculation kW of energy needed for heat up gas
        Q1Heater = Qdot * g.D * (H2 - H1)  # kJ/s
        print("needed power is ", Q1Heater, " kW", " and HHV is ", HHV)
        # change kJ/s to kJ/hr
        Q1Heater = Q1Heater * 3600
        #change kJ/hr to kg/hr
        Q1Heater = Q1Heater / HHV
        # change kg/hr to Standard m^3/hr
        Q1Heater = Q1Heater / Dstd
        return Q1Heater