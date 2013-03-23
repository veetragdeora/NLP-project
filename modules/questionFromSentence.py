#!/usr/bin/python

# questionFromSentence.py
# Authored by Ryhan Hassan | rhassan@andrew.cmu.edu
# Transforms declarative sentences into questions.

import re
import nltk

# GIVEN string sentence
# RETURNS (question string, success boolean)
def transform_IT_IS(sentence):
  if ("It is" in sentence):
    question = sentence.replace("It is", "What is")
    return (question, True)
  return (sentence, False)

def add_questionmark(sentence):
  if (sentence[len(sentence) - 1] == '.'):
    sentence = sentence[:len(sentence) - 1]
  return sentence + "?"

# GIVEN string representing a declarative sentence,
# RETURNS string representing a question.
def transform(sentence):
  sentence = add_questionmark(sentence)   # '.' -> '?'

  (question, success) = transform_IT_IS(sentence)
  if success: return (question, True)

  # Switch PRP and VBZ Be
  BEING = [ "IS", "ARE", "WAS", "WERE"]
  tokens = nltk.word_tokenize(sentence)
  posTag = nltk.pos_tag([tokens[0]])[0]

  #if (tokens[1].upper() in BEING and posTag == 'PRP'):
  if (tokens[1].upper() in BEING):
    tokens = [tokens[1].capitalize(), tokens[0].lower()] + tokens[2:]
    return (" ".join(tokens), True)

  """
  tagged = nltk.pos_tag(tokens)
  entities = nltk.chunk.ne_chunk(tagged)

  (word0, tag0) = tagged[0]
  (word1, tag1) = tagged[1]
  if (tag0 == 'PRP' and tag1 =='VBZ'):
    tokens = [word1.capitalize(), word0.lower()] + tokens[2:]
    return (" ".join(tokens), True)
  """

  return (sentence, False)

# GIVEN list of sentences,
# RETURNS list of questions.
def process(sentences):
  questions = [ ]
  for sentence in sentences:
    (question, success) = transform(sentence)
    if (success): questions.append( question )
  return questions