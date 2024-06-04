# Toxic Comment Prediction using Bi-Directional LSTM with BERT Tokenizer

# Introduction
Online platforms present a serious problem with toxic remarks that impact community dynamics, user experience, and even mental health. Toxic remarks can be automatically identified and filtered out to help reduce these problems and encourage positive online relationships. The goal of this research is to effectively forecast harmful comments by utilizing machine learning and natural language processing (NLP) techniques.

![1_8BdmU3wYefT7vDZRWWOL1Q](https://github.com/Rhariharan2003/Projects/assets/136108485/caf21c5f-afed-41e2-a9c2-d64eca7a0ad8)


# Problem Statement
The main objective of this project is to create a strong model that can accurately recognize harmful comments. Comments that are toxic can take many different forms, such as hate speech, intimidation, threats, or derogatory language. Developing a model that can reliably identify and categorize such harmful activity presents a challenge, allowing platforms to respond appropriately in order to preserve a healthy online environment.

# Dataset:
Using web scraping techniques, the dataset is curated by methodically pulling comments from public postings, threads, and discussions on various social media networks. Using APIs or bespoke web crawlers, the scraping process retrieves publicly accessible content while adhering to platform terms of service and data protection laws.

# Data Preprocessing:

Before being used for model training and analysis, the dataset undergoes preprocessing steps to ensure consistency, quality, and compatibility with machine learning algorithms. Preprocessing tasks may include:

**Text Cleaning**: Removing HTML tags, special characters, URLs, and other noise from the text data.
<br>
<br>
**Tokenization**: Segmenting comments into individual words or tokens for further analysis.
<br>
<br>
**Normalization**: Standardizing text data by converting to lowercase, removing accents, and expanding contractions.
<br>
<br>
**Filtering**: Removing spam, bot-generated content, and irrelevant comments to focus on genuine user interactions.
<br>

# Tokenization Process (BERT transformer)
The input text is tokenized by splitting it up into discrete tokens or subwords, which are then mapped to matching vectors in the embedding space of BERT. In contrast to conventional tokenizers, BERT tokenization takes into account the context of every token in the phrase, making it better able to capture word subtleties and dependencies.

# Model
The Bi-Directional LSTM (Long Short-Term Memory) model is a powerful deep learning architecture commonly used for sequence classification tasks, including text classification. In the context of toxic comment prediction, the model analyzes the textual content of comments to accurately classify them as toxic or non-toxic. By leveraging bidirectional information flow and memory cells, Bi-LSTM models can capture complex patterns and dependencies within the input sequences, leading to more accurate predictions.

# Model Architecture
![model](https://github.com/Rhariharan08/Toxic_Comments_Prediction/blob/main/model.png)


# Performance Evaluation

The performance of the Bi-Directional LSTM model for toxic comment prediction is evaluated using standard evaluation metrics, including:

  **Accuracy**: 87%
  <br>
  <br>
  **Precision**: 81%
  <br>
  <br>
  **Recall**: 94%
  <br>
  <br>
  **F1 Score**: 87%
  <br>
  <br>
