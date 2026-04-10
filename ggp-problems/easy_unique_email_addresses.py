class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        # use a set, will filter out duplicates
        for i in emails:
            split = i.split("@")
            local_name = split[0]
            domain_name = split[1]

            # ignore after + and remove .
            local_name = local_name.split("+")[0]
            cleaned_email = local_name.replace(".", "") + "@" + domain_name

            # add to unique email set
            unique_emails.add(cleaned_email)

        return len(unique_emails)
