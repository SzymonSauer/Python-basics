def isAnagram(word1, word2):
    n = len(word1)
    if n != len(word2):
        return False
    dictionary1 = dict()
    dictionary2 = dict()
    for i in range(n):
        if word1[i] in dictionary1:
            dictionary1[word1[i]] += 1
        else:
            dictionary1[word1[i]] = 1
        if word2[i] in dictionary2:
            dictionary2[word2[i]] += 1
        else:
            dictionary2[word2[i]] = 1
    return dictionary1 == dictionary2

def main():
    print("isAnagram(radar, rrdaa) = " + str(isAnagram("radar", "rrdaa")))
    print("isAnagram(kajak, blabla) = " + str(isAnagram("kajak", "blabla")))

if __name__ == "__main__":
    main()