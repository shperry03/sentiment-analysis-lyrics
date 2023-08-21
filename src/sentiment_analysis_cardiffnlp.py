'''
Using the cardiffnlp/twitter-roberta-base-sentiment-latest llm from hugging face
I found this performed best on the test songs that I wanted to try

you can do this many different ways but I use pytorch and the transfomers library for sentiment analysis

'''
from transformers import AutoTokenizer, AutoModelForSequenceClassification

import torch
import torch.nn.functional as F

# called in main to do sentiment analysis on the scraped lyrics
def sentiment_analysis_cardiffnlp(lyrics):

    # select model from hugging face and set up model and tokenizer
    model_name = 'cardiffnlp/twitter-roberta-base-sentiment-latest'

    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # create the batch that is passed into the model
    batch = tokenizer(lyrics, padding=True, truncation=True, max_length=512, return_tensors='pt')

    with torch.no_grad():
        # unpack batch and run through model
        outputs = model(**batch)

        # get predictions from the output
        predictions = F.softmax(outputs.logits, dim=1)

        # from the predictions, pick the highest one for the label
        labels = torch.argmax(predictions, dim=1)

        # turn the tensor label to the actual label ie "positive", "negative", or "neutral"
        labels = [model.config.id2label[label_id] for label_id in labels.tolist()]
        
        return labels
