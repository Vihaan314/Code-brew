import string
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Define a function for frequency analysis decryption
def frequency_analysis(ciphertext):
    # Define a set of English stop words
    stop_words = set(stopwords.words('english'))

    # Define a dictionary of English letter frequencies
    english_freq = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97,
                    'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25,
                    'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36,
                    'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29,
                    'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10,
                    'z': 0.07}

    # Convert the ciphertext to lowercase
    ciphertext = ciphertext.lower()

    # Remove all non-letter characters from the ciphertext
    ciphertext = ''.join(c for c in ciphertext if c.isalpha())

    # Perform frequency analysis on the ciphertext
    freq = Counter(ciphertext)
    total = sum(freq.values())
    freq = {letter: count / total * 100 for letter, count in freq.items()}

    # Create a list of (letter, frequency) tuples sorted by frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Create a list of possible plaintexts with different mappings
    plaintexts = []
    for i in range(26):
        # Create a mapping of ciphertext letters to plaintext letters
        mapping = {}
        for j in range(len(sorted_freq)):
            mapping[sorted_freq[j][0]] = string.ascii_lowercase[(j + i) % 26]


        # Apply the mapping to the ciphertext
        plaintext = ''.join(mapping.get(c, c) for c in ciphertext)

        # Check if the plaintext contains enough English words
        num_words = len(plaintext.split())
        num_stop_words = sum(1 for word in plaintext.split() if word in stop_words)
        percent_stop_words = (num_stop_words / num_words) * 100
        if percent_stop_words < 50:
            plaintexts.append(plaintext)

    # Choose the plaintext with the most English words
    best_plaintext = max(plaintexts, key=lambda p: sum(1 for word in p.split() if word not in stop_words))

    # If no suitable plaintext was found, return an error message
    if not best_plaintext:
        return 'Unable to decrypt the message'

    return best_plaintext

# Test the function
ciphertext = "Hmjjxj nx f gjqtaji ktti ktw rfsd, fsi ny'x sty mfwi yt xjj bmd. Bnym nyx bnij wfslj tk kqfatwx fsi yjcyzwjx, ymjwj'x f hmjjxj tzy ymjwj ktw jajwdtsj. Kwtr ymj xmfwu yfsl tk hmjiifw yt ymj hwjfrd wnhmsjxx tk gwnj, ymjwj fwj htzsyqjxx afwnjynjx tk hmjjxj yt jsotd. Hmjjxj nx fqxt nshwjingqd ajwxfynqj, rfpnsl ny f xyfuqj nslwjinjsy ns rfsd inkkjwjsy hznxnsjx fwtzsi ymj btwqi. Ny hfs gj rjqyji ts ytu tk uneef, lwfyji tajw ufxyf, tw zxji yt fii f ijqnhntzx yfsl yt f xfsibnhm. Fiinyntsfqqd, hmjjxj nx f lwjfy xtzwhj tk uwtyjns fsi hfqhnzr, rfpnsl ny f mjfqymd fsi xfynxkdnsl xsfhp. Bmjymjw jsotdji ts nyx tbs tw nshtwutwfyji nsyt f inxm, hmjjxj nx f ktti ymfy gwnslx ujtuqj ytljymjw fsi fiix f ijqnhntzx, htrktwynsl jqjrjsy yt fsd rjfq"
plaintext = frequency_analysis(ciphertext)
print(plaintext)
