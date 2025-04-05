import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def generate_insights_from_df(df, context="Generate intelligent, innovative, and sustainable recommendations"):
    try:
        if df.empty:
            return "🚫 No data available to generate insights."

        numeric_cols = df.select_dtypes(include="number").columns
        insights = []

        if numeric_cols.empty:
            return "📎 The dataset does not contain numeric values suitable for analysis."

        # Analyzing numeric trends
        for col in numeric_cols:
            mean_val = df[col].mean()
            std_dev = df[col].std()
            max_val = df[col].max()
            min_val = df[col].min()

            if std_dev < 0.1 * mean_val:
                insights.append(f"📊 **{col}** is stable — optimize around this for resource efficiency.")
            elif max_val > 2 * mean_val:
                insights.append(f"📈 **{col}** has extreme highs — investigate peaks and regulate input usage.")
            elif min_val < 0.5 * mean_val:
                insights.append(f"📉 **{col}** has sharp drops — address causes to avoid risk.")

        # Smart suggestion
        insights.append("\n🧠 **Smart & Sustainable Innovation Suggestion:**")
        insights.append(
            "- Build a real-time **data dashboard** that tracks this dataset’s key metrics.\n"
            "- Use **IoT sensors** for live data collection (e.g., soil, market prices).\n"
            "- Trigger **mobile alerts** when data crosses safe thresholds.\n"
            "- Enable **predictive planning** for farmers and marketers using simple trend rules.\n"
        )

        insights.append(
            "🎯 This empowers users to make informed decisions, avoid losses, and achieve higher sustainability with minimal tech."
        )

        # Final simple recommendation
        insights.append("\n✅ **Final Simple Recommendation:**")
        insights.append(
            "Start small: Use Excel or a mobile app to track 1–2 important values from your dataset daily. "
            "Within a week, you’ll see patterns. Adjust your actions based on those patterns — that’s smart farming/marketing, made simple. 🌱📱"
        )

        return "\n".join(insights)

    except Exception as e:
        return f"⚠️ Error generating smart insights: {e}"




st.title("FarmWise: Smart Insights for Sustainable Agriculture")

st.subheader(".....")
st.subheader("Add filters for you want to choose, and get customizable insights and solutions to the problems.")
st.subheader(".....")


# Button to reset uploads
if st.button("Reset Uploaded Files"):
    for key in ["farmer_file", "market_file"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

# Upload farmer advisor file
farmer_file = st.file_uploader("Choose the farmer advisor file", key="farmer_file", type="csv")
if farmer_file is not None:
    df1 = pd.read_csv(farmer_file)

    st.subheader("Data Preview of Farmer Advisor")
    st.write(df1.head())

    st.subheader("Data Summary")
    st.write(df1.describe())

    st.subheader("Plot Data (Farmer Advisor)")
    apply_filter1 = st.checkbox("Filter Farmer Advisor Data", value=False, key="filter1")

    if apply_filter1:
        categorical_cols1 = [col for col in df1.columns if df1[col].dtype == "object" or df1[col].nunique() < 10]
        selected_column1 = st.selectbox("Select column to filter by", categorical_cols1, key="filter_col1")
        unique_values1 = df1[selected_column1].unique()
        selected_value1 = st.selectbox("Select value", unique_values1, key="filter_val1")
        filtered_df1 = df1[df1[selected_column1] == selected_value1]
    else:
        filtered_df1 = df1

    st.write(filtered_df1)

    x_column = st.selectbox("Select x-axis column", df1.columns, key="x1")
    y_column = st.selectbox("Select y-axis column", df1.columns, key="y1")

    if st.button("Generate Plot", key="plot1"):
        if len(filtered_df1) > 1:
            fig, ax = plt.subplots()
            ax.plot(filtered_df1[x_column], filtered_df1[y_column], marker='o')
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.set_title(f"{y_column} vs {x_column}")
            st.pyplot(fig)
        else:
            st.warning("Not enough data points to generate a plot. Try removing filter or selecting a different filter.")
        


    if st.button("Generate AI Insight (Farmer Advisor)", key="ai1"):
        insight = generate_insights_from_df(filtered_df1, context="Give simple suggestions for farmers based on this data")
        st.markdown("### 🌾 AI Insight:")
        st.write(insight)


# Upload market research file
market_file = st.file_uploader("Choose the market research file", key="market_file", type="csv")
if market_file is not None:
    df2 = pd.read_csv(market_file)

    st.subheader("Data Preview of Market Research")
    st.write(df2.head())

    st.subheader("Data Summary of Market Research")
    st.write(df2.describe())

    st.subheader("Plot Data (Market Research)")
    apply_filter2 = st.checkbox("Filter Market Research Data", value=False, key="filter2")

    if apply_filter2:
        categorical_cols2 = [col for col in df2.columns if df2[col].dtype == "object" or df2[col].nunique() < 10]
        selected_column2 = st.selectbox("Select column to filter by", categorical_cols2, key="filter_col2")
        unique_values2 = df2[selected_column2].unique()
        selected_value2 = st.selectbox("Select value", unique_values2, key="filter_val2")
        filtered_df2 = df2[df2[selected_column2] == selected_value2]
    else:
        filtered_df2 = df2

    st.write(filtered_df2)

    x_column1 = st.selectbox("Select x-axis column", df2.columns, key="x2")
    y_column1 = st.selectbox("Select y-axis column", df2.columns, key="y2")

    if st.button("Generate Plot", key="plot2"):
        if len(filtered_df2) > 1:
            fig, ax = plt.subplots()
            ax.plot(filtered_df2[x_column1], filtered_df2[y_column1], marker='o', color='orange')
            ax.set_xlabel(x_column1)
            ax.set_ylabel(y_column1)
            ax.set_title(f"{y_column1} vs {x_column1}")
            st.pyplot(fig)
        else:
            st.warning("Not enough data points to generate a plot. Try removing filter or selecting a different filter.")
        

    if st.button("Generate AI Insight (Market Research)", key="ai2"):
        insight = generate_insights_from_df(filtered_df2, context="Provide insights related to market trends or improvements")
        st.markdown("### 📈 AI Insight:")
        st.write(insight)
