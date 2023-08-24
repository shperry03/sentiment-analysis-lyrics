'''
This is the program that makes the call to chatgpt

take the lyrics that are negative and make them positive but stupid
'''

import api_key
import openai
# i have my openai api key in a file for security 
openai.api_key = api_key.chat_gpt_access_key

'''
Takes the lyrics and passes the negative ones to gpt 3.5 turbo
'''
def change_sentiment(labels,lyrics) -> dict:
    # track the lyrics that need to be changed and their replacements in a dictionary
    positive_changes = {}

    for x in lyrics: 

        # if the lyric is negative and hasn't already been handled, pass it to chatgpt
            # if it has been handled then we don't want to waste API calls/time, helps with chorus repitition
        if labels[x] == 'negative' and x not in positive_changes:
            #set the dictionary values to the new lyric
            positive_changes[x] = gpt_positivity(x)

    
    return positive_changes

'''
Changes the lyric to be more positive through chatgpt

ChatGPT worked best with this part so I decided to just
make an API call to chatgpt rather than use another huggingface model
'''
def gpt_positivity(lyric):
    
    # prompt for gpt 3.5 turbo 
    prompt = 'Please write the following lyric to be more positive but still match the rhyme and rhythm of the original lyric: "' + lyric + '"'
    # formatting for the llm
    messages = [{'role':'user', 'content':prompt}]
    
    # make a call to the model with our prompt
    response = openai.ChatCompletion.create(
        # gpt 3.5 turbo is cheap, fast and does the jop
        model='gpt-3.5-turbo',
        # pass our prompt
        messages=messages,
        # come on gpt be a little creative
        temperature=0.8
        )
    
    # get the content of the response and return it
    return response.choices[0].message['content']
    