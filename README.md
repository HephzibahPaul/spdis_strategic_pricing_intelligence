# SPDIS — Strategic Pricing Intelligence Simulator

SPDIS is a pricing strategy simulator designed to understand how customers may react to different pricing decisions.  
It uses synthetic e-commerce data to model **value perception**, **price sensitivity**, **competitor impact**, and **revenue outcomes** under multiple business scenarios.

This project reflects how modern pricing & product teams evaluate decisions before launching them in the market.

---

## 📌 What This Project Does
SPDIS answers key business questions:

###  *How sensitive are customers to price changes?*  
###  *How does competitor pricing influence demand?*  
###  *What happens during festival spikes or flash sales?*  
###  *Which price point maximizes revenue?*  
###  *How does value perception affect customer behavior?*

It simulates real-world pricing situations and produces clear insights and recommendations — similar to how a BA would support strategy teams.

---

## 📂 Project Structure 

```
SPDIS/
│
├── src/
│   ├── data_generator.py
│   ├── vps_engine.py
│   ├── sensitivity_matrix.py
│   ├── scenario_engine.py
│   ├── shock_simulator.py
│   ├── price_ladder.py
│   ├── deck_generator.py
│   └── __init__.py
│
├── data/
│   └── spdis_behavioral_data.csv
│
├── charts/
│   ├── demand_vs_price_p1.png
│   └── revenue_curve_p1.png
│
├── notebook/
│   ├── spdis_analysis.ipynb
│   └── spdis_leadership_deck.md
│
├── requirements.txt
├── LICENSE
└── README.md
```

yaml
Copy code

---

##  Key Business Concepts Modeled

### **1. Behavioral Value Perception (VPS)**  
A scoring method that estimates whether customers feel a price is:
- fair  
- too high  
- a good deal  
- influenced by competitor pricing  

VPS helps explain *why* some prices work and others fail.

---

### **2. Price Sensitivity & Elasticity**
SPDIS identifies:
- which customer types are more price-sensitive  
- how demand changes when price increases or decreases  
- how competitor undercutting affects your sales  

This is crucial for pricing decisions, product launches, and discount planning.

---

### **3. Scenario Analysis**
The simulator models five realistic pricing scenarios:

- **Price Increase**
- **Discount Activation**
- **Competitor Price Cut**
- **Festival Uplift**
- **Base Case (No Change)**

Each scenario forecasts:
- demand movement  
- revenue change  
- margin impact  
- customer perception  

---

### **4. Shock Simulation**
Used for short-term, high-impact events such as:
- competitor flash sales  
- festival shopping spikes  
- sudden market disruptions  

BAs use this to stress-test a pricing strategy.

---

### **5. Revenue Curve & Optimal Price**
SPDIS evaluates dozens of price points and finds the approximate point where **revenue is maximized**.

This helps decision-makers choose a price that balances:
- sales volume  
- customer acceptance  
- profitability  

---

##  Example Insights From the Simulator

- Customers in “bargain-driven” segments respond strongly to competitor price drops.  
- Festival season raises demand significantly, but only for specific product types.  
- A mid-tier price point performed best across simulations.  
- Price increases above a threshold created noticeable demand drop-offs.  
- Value Perception Score strongly correlates with buying behavior.

---



## ⭐ Why This Project Matters
Pricing decisions can significantly influence:
- conversion rates  
- revenue  
- customer satisfaction  
- competitive advantage  

SPDIS demonstrates how pricing can be approached analytically using:
- structured data  
- business logic  
- scenario thinking  
- storytelling insights  

It mirrors the type of analysis BAs perform in e-commerce, SaaS, retail, and marketplace companies.

---

## 📄 License  
MIT License — free to use, modify, and distribute.