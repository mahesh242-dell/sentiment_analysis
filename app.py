import streamlit as st
import sentiment
import pandas as pd
from collections import Counter

st.title("Sentiment Analysis")
temp="""
    <div style="background-color:grey; padding:10px">
    <h2 style="color:white; text-align:center;"> Real Time Sentiment Analysis </h2>
    </div>
"""
st.markdown(temp, unsafe_allow_html=True)

if "review_list" not in st.session_state:
    st.session_state["review_list"] = []
if "prediction_list" not in st.session_state:
    st.session_state["prediction_list"] = []
if "positive_count" not in st.session_state:
    st.session_state["positive_count"] = 0
if "negative_count" not in st.session_state:
    st.session_state["negative_count"] = 0
if "neutral_count" not in st.session_state:
    st.session_state["neutral_count"] = 0


text=st.text_input("Text","")
if st.button("Predict"):
    result=sentiment.calculatesentiment(text)
    st.write(f"Debug: Text '{text}' has sentiment '{result}'")
    st.session_state["review_list"].append(text)
    st.session_state["prediction_list"].append(result)
    if result == "Positive😊...":
        st.session_state["positive_count"] += 1
    elif result == "Negative😞...":
        st.session_state["negative_count"] += 1
    else:
        st.session_state["neutral_count"] += 1
    st.success(result)

file_upload = st.file_uploader("Upload a CSV file", type=["csv"])
if file_upload is not None:
    df = pd.read_csv(file_upload)
    if "review" in df.columns:
        st.session_state["review_list"].extend(df["review"].tolist())
        st.session_state["prediction_list"].extend([sentiment.calculatesentiment(review) for review in df["review"]])
        for review, prediction in zip(df["review"], [sentiment.calculatesentiment(review) for review in df["review"]]):
            st.write(f"Debug: Text '{review}' has sentiment '{prediction}'")
        positive_reviews = [review for review, prediction in zip(df["review"], [sentiment.calculatesentiment(review) for review in df["review"]]) if prediction == "Positive"]
        negative_reviews = [review for review, prediction in zip(df["review"], [sentiment.calculatesentiment(review) for review in df["review"]]) if prediction == "Negative"]
        neutral_reviews = [review for review, prediction in zip(df["review"], [sentiment.calculatesentiment(review) for review in df["review"]]) if prediction == "Neutral"]
        st.session_state["positive_count"] += len(positive_reviews)
        st.session_state["negative_count"] += len(negative_reviews)
        st.session_state["neutral_count"] += len(neutral_reviews)
    else:
        st.error("The CSV file must have a column named 'review'.")

if st.session_state["review_list"]:
    overall_sentiment = Counter(st.session_state["prediction_list"]).most_common(1)[0][0]
    st.write(f"Overall Sentiment: {overall_sentiment}")

    st.write(f"Positive reviews: {st.session_state['positive_count']}")
    st.write(f"Negative reviews: {st.session_state['negative_count']}")
    st.write(f"Neutral reviews: {st.session_state['neutral_count']}")

for i, (review, prediction) in enumerate(zip(st.session_state["review_list"], st.session_state["prediction_list"])):
    st.write(f"{i + 1}. {review} - {prediction}")
