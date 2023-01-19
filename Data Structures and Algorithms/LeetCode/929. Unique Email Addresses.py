class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cleanemail = ""
        cleandomain = ""
        hashset = set()
        for email in emails:
            name = email.split("@")[0]
            domain = email.split("@")[1]
            for char in name:
                if char == ".":
                    continue
                if char == "+":
                    break
                cleanemail += char
            cleanemail += "@"
            for char in domain[0:-4]:
                if char == ".":
                    cleanemail = ""
                    break
            cleanemail += domain
            hashset.add(cleanemail)
            cleanemail = ""
        return len(hashset)
