import random
from collections import defaultdict
import numpy as np
import time

def create_markov_wordlist():
  data = ""
  new_words_list = defaultdict(lambda: defaultdict(int))
  with open("words3.txt", "r") as f:
    data = f.read().replace("\n", " ")
  tokenized_words = data.replace(". ", ". $").replace("? ", "? $").replace("! ", "! $").replace(".", " .").replace("?", " ?").replace("!", " !").split(" ")
  last_word = tokenized_words[0].lower()
  for word in tokenized_words[1:]:
    word = word.lower()
    new_words_list[last_word][word] += 1
    last_word = word
  return new_words_list

def walk_graph(graph, start_node=None, first=True):
  if start_node:
    if "." in start_node or "?" in start_node or "!" in start_node:
      return []
  if not start_node:
    start_node = random.choice(list(graph.keys()))
    while "$" not in start_node:
      start_node = random.choice(list(graph.keys()))
  weights = np.array(list(graph[start_node].values()), dtype=np.float64)
  weights /= weights.sum()
  choices = list(graph[start_node].keys())
  chosen_word = np.random.choice(choices, None, p=weights)
  if first:
    return [start_node.replace("$", ""), chosen_word] + walk_graph(graph, start_node=chosen_word, first=False)
  else:
    return [chosen_word] + walk_graph(graph, start_node=chosen_word, first=False)

def make_markov_chain(max_len=None, required=[".", "."]):
  wordlist = create_markov_wordlist()
  chain = ' '.join(walk_graph(wordlist)).replace(" .", ".")
  counter = 0
  while not (required[0] in chain and required[1] in chain):
    chain = ' '.join(walk_graph(wordlist)).replace(" .", ".")
    counter += 1
    print("Try:", counter)
  return chain, counter

start = time.time()
required = input("Word to require? ")
required2 = input("Second word to require? ")
#required3 = input("Third word to require? ")
#required4 = input("Fourth word to require? ")
#required5 = input("Fifth word to require? ")
#chain, tries = make_markov_chain(required=[required, required2])
chain, tries = make_markov_chain(required=[required, required2])
length = int(time.time() - start)
print("Found in %s tries, %ss: " % (tries, length))
print("\n" + chain)
with open("ember-logs.txt", "a") as logs:
  logs.write("Tries: %s | Duration: %s | Result: %s\n" % (tries, length, chain))
