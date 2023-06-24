import re, math
from collections import Counter

def cosine_similarity(text1, text2):
    words1 = re.findall('\w+', text1.lower())
    words2 = re.findall('\w+', text2.lower())

    frequency1 = Counter(words1)
    frequency2 = Counter(words2)

    dot_product = sum(frequency1[word] * frequency2[word] for word in frequency1 if word in frequency2)

    norm1 = math.sqrt(sum(frequency1[word] ** 2 for word in frequency1))
    norm2 = math.sqrt(sum(frequency2[word] ** 2 for word in frequency2))

    if norm1 == 0 or norm2 == 0:
        return 0
    else:
        return dot_product / (norm1 * norm2)


a = "i am a boy"
b = "i ma a girl"
print(cosine_similarity(a, b)*100)