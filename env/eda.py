import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data Load (Replace this with your actual data)
df = pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\Power_predictor\env\household_energy_prediction_data.csv')
# df_hourly, df_daily should be derived as in your Colab code.


df_hourly = df.groupby('hour')[['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']].mean()
df_daily = df.groupby('day')[['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']].mean()



st.set_page_config(page_title="Household Energy Insights", layout="wide")
st.title("🔋 Household Energy Usage Insights")


st.markdown("Explore your energy usage patterns with clear actions to reduce your bills.")

# ----- Plot 1: Peak Hour Submeter Usage -----
st.header("📊 Peak Hour Submeter Consumption")

st.title("🔋 Household Energy Usage Insights")

# Add explanation about Peak Hours
with st.expander("ℹ️ What Are Peak Hours?"):
    st.markdown("""
    **Peak hours** are times of the day when electricity demand is highest—usually **morning (7–10 AM)** and **evening (6–10 PM)**.
    
    ⚠️ During these hours, **electricity prices may be higher** (if you're on a time-of-use plan), and **the grid is under more stress**.

    **Why it matters:**
    - Using lots of energy during peak hours = **higher bills**
    - Shifting usage to off-peak times = **cost savings** + **helps prevent power cuts**

    💡 **Tip:** Reduce heavy appliance use during peak hours for better savings.
    """)


# Create Peak Hour Plot
peak_hour_df = df[df['peak_hour'] == 1]
submeter_peak_consumption = peak_hour_df.groupby('hour')[['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']].mean()

fig1, ax1 = plt.subplots(figsize=(12, 6))
submeter_peak_consumption.plot(kind='bar', ax=ax1)
ax1.set_title('Average Submeter Consumption During Peak Hours')
ax1.set_xlabel('Hour of Day')
ax1.set_ylabel('Average Energy Consumption (Wh)')
ax1.grid(axis='y')
st.pyplot(fig1)

# Insight + Advice
st.subheader("🔎 Observation:")
st.write("""
Sub_metering_3 (Water Heater & AC) uses the most energy during peak hours, especially between **7–9 AM** and **7–10 PM**.
""")
st.subheader("✅ What You Can Do:")
st.write("""
- Set AC to a higher temperature (e.g., 26°C) and use fans when possible.
- Use timer plugs for water heaters to run only when needed.
- Avoid using other heavy appliances during these hours.
""")

# ----- Plot 2: Daily Usage Pattern -----
st.header("📅 Daily Usage Pattern")

daily_usage = df_hourly.groupby('hour')[['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']].mean()

fig2, ax2 = plt.subplots(figsize=(12, 6))
daily_usage.plot(ax=ax2)
ax2.set_title('Average Daily Submeter Usage Pattern')
ax2.set_xlabel('Hour of Day')
ax2.set_ylabel('Average Submeter Consumption')
ax2.grid(True)
st.pyplot(fig2)

st.subheader("🔎 Observation:")
st.write("""
Energy usage **peaks in the morning (7–10 AM)** and **evening (6–10 PM)** due to water heating, AC, and cooking.
""")
st.subheader("✅ What You Can Do:")
st.write("""
- Shift laundry/dishwashing to **midday or night** to reduce load during peaks.
- Combine small cooking tasks to reduce kitchen energy use.
""")

# ----- Plot 3: Weekly Usage -----
st.header("🗓️ Weekly Usage Pattern")

weekly_usage = df.groupby('weekday')[['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']].mean()

fig3, ax3 = plt.subplots(figsize=(12, 6))
weekly_usage.plot(ax=ax3)
ax3.set_title('Average Weekly Submeter Usage Pattern')
ax3.set_xlabel('Day of Week (0=Mon, 6=Sun)')
ax3.set_ylabel('Average Submeter Consumption')
ax3.set_xticks(range(7))
ax3.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
ax3.grid(True)
st.pyplot(fig3)

st.subheader("🔎 Observation:")
st.write("""
Energy usage increases on **weekends**, especially on **Saturday** for laundry and AC use.
""")
st.subheader("✅ What You Can Do:")
st.write("""
- Run washing machines earlier on weekends to avoid peak rates.
- Space out heavy appliance usage over both weekend days.
""")

# ----- Plot 4: Monthly/Seasonal Usage -----
st.header("📆 Monthly (Seasonal) Usage Pattern")

monthly_usage = df.groupby('month')[['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']].mean()

fig4, ax4 = plt.subplots(figsize=(12, 6))
monthly_usage.plot(ax=ax4)
ax4.set_title('Average Monthly Submeter Usage Pattern')
ax4.set_xlabel('Month')
ax4.set_ylabel('Average Submeter Consumption')
ax4.set_xticks(range(1, 13))
ax4.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax4.grid(True)
st.pyplot(fig4)

st.subheader("🔎 Observation:")
st.write("""
**Energy usage dips in July–August** (monsoon) and increases in **hot months** (summer) and cooler months (for water heating).
""")
st.subheader("✅ What You Can Do:")
st.write("""
- In summer: Use curtains, fans, and clean AC filters.
- In winter: Use water heater only when needed; switch off when not in use.
""")

# ----- Plot 5: Yearly Comparison -----
st.header("📈 Yearly Usage Comparison")

yearly_usage = df.groupby('year')[['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']].mean()

fig5, ax5 = plt.subplots(figsize=(12, 6))
yearly_usage.plot(marker='o', ax=ax5)
ax5.set_title('Average Yearly Submeter Usage Comparison')
ax5.set_xlabel('Year')
ax5.set_ylabel('Average Submeter Consumption')
ax5.grid(True)
st.pyplot(fig5)

# Add Your Final Summary
st.header("📌 Overall Advice for You")
st.markdown("""
- Focus on **water heater & AC usage** – they are the biggest contributors.
- **Shift heavy usage** (laundry, dishwashing) to off-peak hours.
- Maintain your AC and heater for better efficiency.
- Use energy-efficient kitchen and laundry appliances for long-term savings.
""")
