# /d for int and /s for string
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