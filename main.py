import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():

    url = utext.get("1.0","end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    title.delete('1.0','end')
    title.insert('1.0',article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0','end')
    sentiment.insert('1.0',f'Polarity {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negetive" if analysis.polarity < 0 else "neutral"} ')

    title.config(state="disabled")
    author.config(state="disabled")
    publication.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")


root = tk.Tk()
root.title("News Summerizer")
root.geometry("1000x600")

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=120)
title.config(state="disabled", bg= "#dddddd")
title.pack()

alable = tk.Label(root, text="Author")
alable.pack()

author = tk.Text(root, height=1, width=120)
author.config(state="disabled",bg="#dddddd")
author.pack()

plable = tk.Label(root, text="Publication Date")
plable.pack()

publication = tk.Text(root, height=1, width=120)
publication.config(state="disabled",bg="#dddddd")
publication.pack()

slable = tk.Label(root, text="Summary")
slable.pack()

summary = tk.Text(root, height=20, width=120)
summary.config(state="disabled",bg="#dddddd")
summary.pack()

selable = tk.Label(root, text="Sentiment Analysis")
selable.pack()

sentiment = tk.Text(root, height=1, width=120)
sentiment.config(state="disabled",bg="#dddddd")
sentiment.pack()

ulable = tk.Label(root, text="URL")
ulable.pack()

utext = tk.Text(root, height=1, width=120)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()