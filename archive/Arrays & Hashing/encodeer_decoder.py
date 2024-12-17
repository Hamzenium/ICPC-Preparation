class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        for index in range(len(strs)):
            if(index == 0):
                output += "".join(strs[index])
            else:
                output += "@^@^&"
                output += "".join(strs[index])
        return output
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        return s.split('@^@^&')
    
encoder = Codec()
array = ["@","Z","2>h(lF:w",""]
print(array)
value = encoder.encode(array)
print(encoder.encode(array))
print(encoder.decode(value))
