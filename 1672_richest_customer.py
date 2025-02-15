class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for account in accounts:
            if sum(account) > max_sum:
                max_sum = sum(account)
        return max_sum