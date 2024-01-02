'''
def word_split(phrase,list_of_words,output= None):
  if output is None:
    output = []

  for word in list_of_words:
    if phrase.startswith(word):
      output.append(word)

      return word_split(phrase[len(word):],list_of_words,output)

  return output

s1 = word_split('themanran',['the','ran','man'])
s2 = word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
s3 = word_split('themanran',['clown','ran','man'])
print(s1)
print(s2)
print(s3)
'''
def reverse(s):
  if len(s) <=1:
    return s  
  return reverse(s[1:])+s[0]

r = reverse('hello world')
print(r)