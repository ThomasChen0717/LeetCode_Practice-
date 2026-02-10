# Approach 1: DFS
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        visited = set() 

        account_mp = collections.defaultdict(list) 

        res = []

        def dfs(root, lst): 

            lst.append(root) 
            visited.add(root)

            for neighbor in account_mp[root]: 
                if neighbor not in visited: 
                    dfs(neighbor, lst)

        
        for account in accounts: 
            account_size = len(account)


            first_acc = account[1] 

            for i in range(2, account_size): 
                curr_acc = account[i]
                account_mp[first_acc].append(curr_acc)
                account_mp[curr_acc].append(first_acc) 

        for account in accounts: 
            name = account[0] 

            if account[1] not in visited: 
                email_list = []
                dfs(account[1], email_list) 
                res.append([name] + sorted(email_list))
             
        return res

# Approach 2: Union Find
class UnionFind: 
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x): 
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y): 
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY: return 

        if self.size[rootX] < self.size[rootY]: 
            rootX, rootY = rootY, rootX
        
        self.parent[rootY] = rootX 
        self.size[rootX] += self.size[rootY] 


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)

        email_group = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_group:
                    email_group[email] = i
                else:
                    uf.union(i, email_group[email])
        
        components = collections.defaultdict(list)
        for email, idx in email_group.items():
            root = uf.find(idx)
            components[root].append(email)

        # 3️⃣ Build result
        merged = []
        for root, emails in components.items():
            merged.append([accounts[root][0]] + sorted(emails))

        return merged
        

