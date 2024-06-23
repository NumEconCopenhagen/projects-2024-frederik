from types import SimpleNamespace

class ExchangeEconomyClass:
    def __init__(self):
        par = self.par = SimpleNamespace()

        # Preferences
        par.alpha = 1/3
        par.beta = 2/3

        # Endowments
        par.w1A = 0.8
        par.w2A = 0.3
        par.w1B = 1-par.w1A  # Assuming endowment for B as it's missing
        par.w2B = 1-par.w2A  # Assuming endowment for B as it's missing
    

    def utility_A(self, x1A, x2A):
        alpha = self.par.alpha
        return x1A**alpha * x2A**(1-alpha)

    def utility_B(self, x1B, x2B):
        beta = self.par.beta
        return x1B**beta * x2B**(1-beta)

    def demand_A(self, p1):
        par = self.par
        alpha = par.alpha
        w1A = par.w1A
        w2A = par.w2A
        return alpha * ((p1 * w1A + w2A) / p1)

    def demand_B(self, p1):
        par = self.par
        beta = par.beta
        w1B = par.w1B
        w2B = par.w2B
        return beta * ((p1 * w1B + w2B) / p1)

    def check_market_clearing(self, p1):
        par = self.par

        x1A = self.demand_A(p1)
        x2A = 1-self.demand_A(p1)
        x1B = self.demand_B(p1)
        x2B = 1-self.demand_B(p1)
        
        eps1 = x1A - par.w1A + x1B - (1 - par.w1A)
        eps2 = x2A - par.w2A + x2B - (1 - par.w2A)  

        return eps1, eps2

