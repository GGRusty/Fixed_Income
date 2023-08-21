from datetime import datetime

class Bond:
    def __init__(self, par_value, purchase_price, purchase_date, maturity_date, coupon_rate, payment_frequency):
        self.par_value = par_value
        self.purchase_price = purchase_price
        self.purchase_date = datetime.strptime(purchase_date, "%m-%d-%Y")
        self.maturity_date = datetime.strptime(maturity_date, "%m-%d-%Y")
        self.coupon_rate = coupon_rate
        self.payment_frequency = payment_frequency
        self.annual_coupon = self.face_value * self.coupon_rate
        self.coupon_per_period = self.annual_coupon / self.payment_frequency
    
    
class ZeroCouponBond:
    def __init__(self, face_value, maturity_years):
        self.face_value = face_value
        self.maturity_years = maturity_years
    
    def price(self, yield_rate):
        # Price = Face Value / (1 + yield rate) ** maturity years
        return self.face_value / (1 + yield_rate) ** self.maturity_years