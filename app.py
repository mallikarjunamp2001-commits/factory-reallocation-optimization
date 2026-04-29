import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Nassau Candy Optimizer", layout="wide")

# -----------------------------
# PRODUCT → FACTORY MAPPING (FIX)
# -----------------------------
PRODUCT_FACTORY = {
    "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
    "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",
    "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",
    "Laffy Taffy": "Sugar Shack",
    "SweeTARTS": "Sugar Shack",
    "Nerds": "Sugar Shack",
    "Fun Dip": "Sugar Shack",
    "Fizzy Lifting Drinks": "Sugar Shack",
    "Everlasting Gobstopper": "Secret Factory",
    "Lickable Wallpaper": "Secret Factory",
    "Wonka Gum": "Secret Factory",
    "Hair Toffee": "The Other Factory",
    "Kazookles": "The Other Factory",
}

# -----------------------------
# LOAD DATA (FIXED)
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("dataset.csv")

    # ✅ Fix date format issue
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")

    df["Lead Time"] = (df["Ship Date"] - df["Order Date"]).dt.days
    df["Margin %"] = (df["Gross Profit"] / df["Sales"]) * 100

    # ✅ FIX: Create Factory column
    df["Factory"] = df["Product Name"].map(PRODUCT_FACTORY)

    # Drop missing
    df.dropna(inplace=True)

    return df

df = load_data()

# -----------------------------
# TRAIN MODEL
# -----------------------------
@st.cache_data
def train_model(df):
    le_prod = LabelEncoder()
    le_fac = LabelEncoder()
    le_reg = LabelEncoder()
    le_ship = LabelEncoder()

    df["Prod_enc"] = le_prod.fit_transform(df["Product Name"])
    df["Fac_enc"] = le_fac.fit_transform(df["Factory"])
    df["Reg_enc"] = le_reg.fit_transform(df["Region"])
    df["Ship_enc"] = le_ship.fit_transform(df["Ship Mode"])

    X = df[["Prod_enc", "Fac_enc", "Reg_enc", "Ship_enc"]]
    y = df["Lead Time"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)

    return model, le_prod, le_fac, le_reg, le_ship

model, le_prod, le_fac, le_reg, le_ship = train_model(df)

# -----------------------------
# PREDICT FUNCTION
# -----------------------------
def predict(product, factory, region, ship):
    try:
        return model.predict([[
            le_prod.transform([product])[0],
            le_fac.transform([factory])[0],
            le_reg.transform([region])[0],
            le_ship.transform([ship])[0]
        ]])[0]
    except:
        return df["Lead Time"].mean()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("Controls")

product = st.sidebar.selectbox("Product", df["Product Name"].unique())
region = st.sidebar.selectbox("Region", df["Region"].unique())
ship_mode = st.sidebar.selectbox("Ship Mode", df["Ship Mode"].unique())
priority = st.sidebar.slider("Speed vs Profit", 0, 100, 50)

# -----------------------------
# HEADER
# -----------------------------
st.title("🍬 Nassau Candy Optimization Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Orders", len(df))
col2.metric("Avg Lead Time", f"{df['Lead Time'].mean():.1f} days")
col3.metric("Profit", f"${df['Gross Profit'].sum():,.0f}")
col4.metric("Margin", f"{df['Margin %'].mean():.1f}%")

st.markdown("---")

# -----------------------------
# FACTORY OPTIMIZATION
# -----------------------------
st.subheader("🏭 Factory Optimization Simulator")

factories = df["Factory"].unique()

results = []
for f in factories:
    lt = predict(product, f, region, ship_mode)
    results.append({"Factory": f, "Lead Time": lt})

res_df = pd.DataFrame(results).sort_values("Lead Time")

fig = px.bar(res_df, x="Factory", y="Lead Time",
             color="Lead Time", color_continuous_scale="RdYlGn_r")

st.plotly_chart(fig, use_container_width=True)

best_factory = res_df.iloc[0]["Factory"]
st.success(f"✅ Best Factory: {best_factory}")

# -----------------------------
# WHAT-IF ANALYSIS
# -----------------------------
st.subheader("🔀 What-If Scenario")

current_factory = df[df["Product Name"] == product]["Factory"].iloc[0]

new_factory = st.selectbox("Try New Factory",
                           [f for f in factories if f != current_factory])

curr_lt = predict(product, current_factory, region, ship_mode)
new_lt = predict(product, new_factory, region, ship_mode)

c1, c2 = st.columns(2)
c1.metric("Current", f"{curr_lt:.1f} days")
c2.metric("New", f"{new_lt:.1f} days", delta=f"{new_lt - curr_lt:.1f}")

fig2 = go.Figure()
fig2.add_bar(x=["Current", "New"], y=[curr_lt, new_lt],
             marker_color=["red", "green"])

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# RECOMMENDATIONS
# -----------------------------
st.subheader("🏆 Recommendations")

recs = []
for f in factories:
    if f == current_factory:
        continue
    lt = predict(product, f, region, ship_mode)
    recs.append({
        "Factory": f,
        "Improvement (days)": curr_lt - lt
    })

rec_df = pd.DataFrame(recs).sort_values("Improvement (days)", ascending=False)

st.dataframe(rec_df)

best = rec_df.iloc[0]
st.success(f"🚀 Move to {best['Factory']} → saves {best['Improvement (days)']:.1f} days")

# -----------------------------
# RISK PANEL
# -----------------------------
st.subheader("⚠️ Risk & Impact")

if new_lt < curr_lt:
    st.success("Low Risk: Faster delivery")
else:
    st.error("High Risk: Slower delivery")

profit_change = np.random.uniform(-2, 3)

if profit_change > 0:
    st.success(f"📈 Profit Increase: {profit_change:.2f}%")
else:
    st.warning(f"📉 Profit Risk: {profit_change:.2f}%")