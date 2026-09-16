class Solution:
    def numUniqueEmails(self, emails):
        unique = set()

        for email in emails:
            local, domain = email.split("@")

            # Ignore everything after '+'
            local = local.split("+")[0]

            # Remove all '.'
            local = local.replace(".", "")

            unique.add(local + "@" + domain)

        return len(unique)
