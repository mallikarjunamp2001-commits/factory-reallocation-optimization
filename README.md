# factory-reallocation-optimization
This project is a data-driven decision intelligence system that analyzes factory and shipping operations to optimize product allocation, reduce shipping costs, and improve overall efficiency using machine learning techniques and visualization dashboards.

### Nassau Candy Distributor – Decision Intelligence Project

---

## 📌 Project Overview

This project is a **machine learning-powered decision intelligence system** designed to optimize factory allocation and shipping performance for Nassau Candy Distributor.

It helps transform static logistics decisions into **data-driven optimized recommendations** by:

* 📦 Predicting shipping lead times under different configurations
* 🏭 Recommending optimal factory assignments for products
* 💰 Balancing shipping efficiency and profitability
* 📊 Simulating multiple operational scenarios before execution

---

## 🎯 Problem Statement

Nassau Candy currently relies on static rules for assigning products to factories, leading to:

* High shipping delays in multiple regions
* Inefficient logistics routing
* Increased operational cost and reduced profit margins
* No system to evaluate alternative factory assignments

👉 This project introduces an **AI-based optimization and decision support system**.

---

## 🧠 Solution Approach

The system uses machine learning and optimization techniques to:

1. Predict shipping lead time
2. Analyze factory-product-region relationships
3. Simulate alternative factory assignments
4. Recommend best factory allocation based on performance

---

## 📊 Dataset Description

| Field          | Description                      |
| -------------- | -------------------------------- |
| Row ID         | Unique identifier for each row   |
| Order ID       | Unique order reference           |
| Order Date     | Date when order was placed       |
| Ship Date      | Date when order was shipped      |
| Ship Mode      | Mode of shipping used            |
| Customer ID    | Unique customer identifier       |
| Country/Region | Customer location country/region |
| City           | Customer city                    |
| State/Province | Customer state                   |
| Postal Code    | Postal code of customer          |
| Division       | Product division category        |
| Region         | Sales region                     |
| Product ID     | Unique product identifier        |
| Product Name   | Name of product                  |
| Sales          | Total sales value                |
| Units          | Quantity ordered                 |
| Gross Profit   | Profit (Sales - Cost)            |
| Cost           | Manufacturing cost               |

---

## 🧠 Methodology

### 1. Data Preprocessing

* Handling missing values
* Encoding categorical variables
* Outlier removal
* Feature scaling

---

### 2. Machine Learning Models

* Linear Regression (baseline)
* Random Forest Regressor
* Gradient Boosting Regressor

**Target Variable:** Shipping Lead Time

---

### 3. Model Evaluation Metrics

* RMSE (Root Mean Squared Error)
* MAE (Mean Absolute Error)
* R² Score

---

### 4. Route & Product Analysis

* Clustering of similar shipping routes
* Identification of bottlenecks
* Detection of slow-performing regions

---

### 5. Scenario Simulation Engine

* Simulates product reassignment across factories
* Predicts new shipping lead times
* Measures operational improvement
* Evaluates profit impact

---

### 6. Optimization Logic

Recommendations are generated based on:

* ⏱ Lead time reduction
* 💰 Profit impact
* ⚠ Risk level
* 📈 Operational efficiency

---

## 📈 Key Performance Indicators (KPIs)

| KPI                     | Description                   |
| ----------------------- | ----------------------------- |
| Lead Time Reduction (%) | Improvement in shipping speed |
| Profit Impact Score     | Financial improvement measure |
| Scenario Confidence     | Model reliability score       |
| Recommendation Coverage | System scalability metric     |

---

## 🌐 Streamlit Web Application

### 📊 Features

* Factory Optimization Simulator
* What-If Scenario Analysis
* Recommendation Dashboard
* Risk & Impact Analysis Panel

---

### 🎛 User Controls

* Product selection
* Region filtering
* Ship mode selection
* Optimization priority (speed vs profit)

---

## 🏭 Factory Coordinates

| Factory           | Latitude  | Longitude   |
| ----------------- | --------- | ----------- |
| Lot’s O’ Nuts     | 32.881893 | -111.768036 |
| Wicked Choccy’s   | 32.076176 | -81.088371  |
| Sugar Shack       | 48.11914  | -96.18115   |
| Secret Factory    | 41.446333 | -90.565487  |
| The Other Factory | 35.1175   | -89.971107  |

---

## 🔗 Product–Factory Mapping

### 🍫 Chocolate Division

* Wonka Bar - Nutty Crunch Surprise → Lot’s O’ Nuts
* Wonka Bar - Milk Chocolate → Wicked Choccy’s

### 🍬 Sugar Division

* Laffy Taffy → Sugar Shack
* Nerds → Sugar Shack
* Fun Dip → Sugar Shack

### 🍭 Other Products

* Lickable Wallpaper → Secret Factory
* Hair Toffee → The Other Factory

---

## 🚀 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Streamlit
* plotly

---

## ⚙️ How to Run Project

```bash
# Clone repository
git clone https://github.com/your-username/factory-reallocation.git

# Enter folder
cd factory-reallocation

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---

## 📌 Conclusion

This project transforms logistics operations from **static rule-based decision-making** into an **AI-powered optimization system**, improving:

* Shipping efficiency
* Profitability
* Operational planning

---

## 🌐 Demo / Live Project

If deployed, you can access the live application here:

🔗 **Demo Link:** 
https://mallikarjunamp2001-commits-factory-reallocation-opti-app-v6vuht.streamlit.app/



---

## 👨‍💻 Author

Mallikarjuna M P

Machine Learning & Supply Chain Optimization Project
