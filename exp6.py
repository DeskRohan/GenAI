from transformers import pipeline

analyzer = pipeline("sentiment-analysis")

reviews = [
    "The new phone I bought is absolutely amazing!",
    "Worst customer service ever.",
    "The experience was average.",
    "Fast delivery and perfect packaging.",
    "The product broke within two days."
]

for text, result in zip(reviews, analyzer(reviews)):
    print(f"{text}\n{result['label']} ({result['score']:.2f})\n")
