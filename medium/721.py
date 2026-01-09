class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_name = {}
        graph = defaultdict(set)

        for account in accounts:
            name = account[0]
            first = account[1]
            for email in account[1:]:
                graph[first].add(email)
                graph[email].add(first)
                email_name[email] = name
        
        visited = set()
        merged = []

        def dfs(email, emails):
            if email in visited:
                return
            visited.add(email)
            emails.append(email)
            for neighbor in graph[email]:
                dfs(neighbor, emails)

        for email in graph:
            if email not in visited:
                emails = []
                dfs(email,emails)
                merged.append([email_name[email]] + sorted(emails))

        return merged