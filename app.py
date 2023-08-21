import streamlit as st
import matplotlib.pyplot as plt
from bond_calculations import ZeroCouponBond
import numpy as np

st.title("Zero Coupon Bond - Price to Yield Relationship")

face_value = st.number_input("Face Value ($)", min_value=100.0, max_value=10000.0, value=1000.0)
maturity_years = st.slider("Maturity (Years)", min_value=1, max_value=30, value=10)
min_yield = st.slider("Minimum Yield (%)", min_value=0.0, max_value=20.0, value=0.0, step=0.1)
max_yield = st.slider("Maximum Yield (%)", min_value=0.0, max_value=20.0, value=10.0, step=0.1)

bond = ZeroCouponBond(face_value=face_value, maturity_years=maturity_years)

# Generate data for graph
yields = np.linspace(min_yield / 100, max_yield / 100, 100)
prices = [bond.price(y) for y in yields]

# # Plotting
fig, ax = plt.subplots()
ax.plot(yields * 100, prices)
ax.set_title("Price vs Yield")
ax.set_xlabel("Yield (%)")
ax.set_ylabel("Price ($)")

st.pyplot(fig)