""" 
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

"""
import string


class Completer:
    
    def __init__(self):
        self.dictionary = {}
        for s in string.ascii_lowercase:
            self.dictionary[s] = set()
    
    def add_term_to_dict(self, term):
        lowered = term.lower()
        self.dictionary[lowered[0]].add(lowered)
    
    def add_terms(self, terms):
        for t in terms:
            self.add_term_to_dict(t)

    def match(self, s1, s2):
        return s1 == s2[:len(s1)]
    
    def query(self, s):
        response = []
        for term in self.dictionary[s[0]]:
            if self.match(s, term):
                response.append(term)
        return response


####

if __name__ == '__main__':

    c = Completer()

    assert c.match("de", "deer") == True
    assert c.match("de", "door") == False

    c.add_term_to_dict("deer")
    c.add_terms(["dog", "deer", "deal"])
    c.query("de")   