lower_cases="abcdefghijklmnopqrstuvwxyz"
upper_cases=lower_cases.upper()

class Makepattern:
    def __init__(self, pattern):
        if not pattern:
            raise Exception("Please define the pattern")
        self.pattern = []
        self.specials = ["/d", "/s"]\

        # Making the pattern
        if len(pattern) > 1:
            for i in range(len(pattern)):
                if i == 0:
                    if pattern[i] + pattern[i+1] in self.specials:
                        self.pattern.append(pattern[i] + pattern[i+1])
                    else:
                        self.pattern.append(pattern[i])
                elif i == len(pattern)-1:
                    if pattern[i-1] + pattern[i] in self.specials:
                        continue
                    else:
                        self.pattern.append(pattern[i])
                else:
                    if pattern[i-1] + pattern[i] in self.specials:
                        continue
                    elif pattern[i] + pattern[i+1] in self.specials:
                        self.pattern.append(pattern[i] + pattern[i+1])
                    else:
                        self.pattern.append(pattern[i])
        else:
            self.pattern.append(pattern[i])

    # Making the function search for the pattern in the text  
    def search(self, text):
        length = len(self.pattern)
        if len(text) < length:
            return False
        elif len(text) == length:
            for p, s in zip(self.pattern, text):
                if p in self.specials:
                    if p == "/d":
                        if not s.isdigit():
                            return False
                    else:
                        if s.isdigit():
                            return False
                else:
                    if p != s:
                        return False
        for i in range(len(text)-length+1):
            passed = False
            section = text[i:i+length]
            now = True
            for p, s in zip(self.pattern, section):
                if p in self.specials:
                    if p == "/d":
                        if not s.isdigit():
                            now = False
                    else:
                        if s.isdigit():
                            now = False
                else:
                    if p != s:
                        now = False
            if now:
                passed = True
                break
        return passed

    def overwrite(self, text, new_text):
        length = len(self.pattern)
        if len(text) < length:
            raise Exception("Invalid Input")

        elif len(text) == length:
            if self.search(text):
                return new_text
            else:
                return text
        
        for i in range(len(text)-length+1):
            section = text[i:i+length]
            if self.search(section):
                result = text[:i] + new_text + text[i+length:]
                return result
            else:
                continue
        return text


def search(pattern, text):
    pat = Makepattern(pattern)
    result = pat.search(text)
    return result

def overwrite(pattern, text, new_text):
    pat = Makepattern(pattern)
    result = pat.overwrite(text, new_text)
    return result

def rot13_encode(text):
    result = ""
    for letter in text:
        if letter in lower_cases:
            i = lower_cases.index(letter)
            if i < len(lower_cases)-1-13:
                result += lower_cases[i+13]
            else:
                result += lower_cases[i+13-len(lower_cases)]
        elif letter in upper_cases:
            i = upper_cases.index(letter)
            if i < len(upper_cases)-1-13:
                result += upper_cases[i+13]
            else:
                result += upper_cases[i+13-len(upper_cases)]
        else:
            result += letter
    return result

def rot13_decode(text):
    result = ""
    for letter in text:
        if letter in lower_cases:
            i = lower_cases.index(letter)
            if i > 12:
                result += lower_cases[i-13]
            else:
                result += lower_cases[i-13+len(lower_cases)]
        elif letter in upper_cases:
            i = upper_cases.index(letter)
            if i > 12:
                result += upper_cases[i-13]
            else:
                result += upper_cases[i-13+len(upper_cases)]
        else:
            result += letter
    return result

def rotx_encode(text, n):
    if len(lower_cases) <= n:
        n -= len(lower_cases)
    result = ""
    for letter in text:
        if letter in lower_cases:
            i = lower_cases.index(letter)
            if i < len(lower_cases)-1-n:
                result += lower_cases[i+n]
            else:
                result += lower_cases[i+n-len(lower_cases)]
        elif letter in upper_cases:
            i = upper_cases.index(letter)
            if i < len(upper_cases)-1-n:
                result += upper_cases[i+n]
            else:
                result += upper_cases[i+n-len(upper_cases)]
        else:
            result += letter
    return result

def rotx_decode(text, n):
    if len(lower_cases) <= n:
        n -= len(lower_cases)
    result = ""
    for letter in text:
        if letter in lower_cases:
            i = lower_cases.index(letter)
            if i > n-1:
                result += lower_cases[i-n]
            else:
                result += lower_cases[i-n+len(lower_cases)]
        elif letter in upper_cases:
            i = upper_cases.index(letter)
            if i > n-1:
                result += upper_cases[i-n]
            else:
                result += upper_cases[i-n+len(upper_cases)]
        else:
            result += letter
    return result

def filter_int(text):
    result = ""
    for letter in text:
        if letter.isdigit():
            result += letter
    return int(result)

def filter_str(text):
    result = ""
    for letter in text:
        if not letter.isdigit():
            result += letter
    return result

def reverse_str(text):
    return ''.join(list(text)[::-1])
