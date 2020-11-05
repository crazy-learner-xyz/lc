class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emails_new = []
        for e in emails:
            e_lst = e.split("@")
            local_name = e_lst[0]
            domain_name = e_lst[1]
            e_lst = local_name.split("+")
            e_lst = e_lst[0].split(".")
            local_name_new = ''.join(e_lst)
            emails_new.append(local_name_new+"@"+domain_name)
        
        emails_set = set(emails_new)
        emails_res = list(emails_set)
        return len(emails_res)

