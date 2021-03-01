"""
Write a function between_len that takes three arguments:
    a list words;
    an integer minlen; and
    an integer maxlen.
The function should return True if the length of words is at least minlen 
and no more than maxlen, and False otherwise.
"""

"""def max_len(a):
    my_list = [a]
    my_list.len()
    if a.len()<=maxlen and a.len>=minlen:
        return True
    else:
        return False
print(max_len(a))"""

"""def find_longest_word(words_list):
    word_len = []
    for n in words_list:
	    word_len.append((len(n), n))
	    word_len.sort()
	    return word_len[-1][1]
	
print(find_longest_word(["PHP", "Exercises", "Backend"]))"""

def max_len(words_list):
    word_len = []
    for n in words_list:
        if word_len.len()<=maxlen and word_len.len>=minlen:
            return True
        else:
            return False

print(max_len(["python"]))