from transformers import pipeline

# Load the pre-trained sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

customer_feedback = [
        "The product is amazing! I love it!",
        "Terrible service, I am very disappointed.",
        "This is a great experience, I will buy again.",
        "Worst purchase I’ve ever made. Completely dissatisfied.",
        "I'm happy with the quality, but the delivery was delayed."
    ]

for feedback in customer_feedback:
        sentiment_result = sentiment_analyzer(feedback)
        sentiment_label = sentiment_result[0]['label']
        sentiment_score = sentiment_result[0]['score']
        
        # Display sentiment results
        print(f"Feedback: {feedback}")
        print(f"Sentiment: {sentiment_label} (Confidence: {sentiment_score:.2f})\n")
