import pandas as pd
import sqlite3
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Gaming Analytics Dashboard", page_icon="🎮", layout="wide"
)

# Dashboard Header
st.title("🎮 Gaming Analytics Dashboard")
st.markdown(
    "A professional dashboard connected to a local SQLite database, providing"
    " live insights into video games."
)
st.divider()


# Load Data directly from the local SQLite database
def load_data():
  try:
    conn = sqlite3.connect("games_database.db")
    df = pd.read_sql("SELECT * FROM games", conn)
    conn.close()
    return df
  except Exception as e:
    st.error(f"Database Connection Error: {e}")
    return pd.DataFrame()


# Fetch Data
df = load_data()

if not df.empty:
  # --- Key Metrics Section ---
  st.subheader("📊 Quick Overview")
  col1, col2, col3 = st.columns(3)

  with col1:
    st.metric(label="Total Games", value=len(df))
  with col2:
    st.metric(label="Supported Platforms", value=df["platform"].nunique())
  with col3:
    st.metric(label="Game Genres", value=df["genre"].nunique())

  st.divider()

  # --- Filter Section ---
  st.subheader("🔍 Explore & Filter Games")
  genres_list = ["All Genres"] + sorted(list(df["genre"].dropna().unique()))
  selected_genre = st.selectbox("Filter by Genre:", genres_list)

  if selected_genre != "All Genres":
    filtered_df = df[df["genre"] == selected_genre]
  else:
    filtered_df = df

  # --- 1. Display Games Table ---
  st.write("### 📋 Games List")
  st.dataframe(filtered_df, use_container_width=True, height=400)

  st.divider()

  # --- 2. Display Chart ---
  st.subheader("📈 Top Game Genres Distribution")
  genre_counts = df["genre"].value_counts().head(10)
  st.bar_chart(genre_counts)

else:
  st.warning(
      "No data found in 'games_database.db'. Please check your database file!"
  )


