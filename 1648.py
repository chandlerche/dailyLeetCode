class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        ans = 0
        inventory = sorted(inventory, reverse=True)
        index = 0
        while orders > 0:
            while index < len(inventory) - 1 and inventory[index] == inventory[index + 1]:
                index += 1
            if index!= len(inventory)-1:
                if orders > (index+1)*(inventory[index]-inventory[index+1]):
                    orders -= (index+1)*(inventory[index]-inventory[index+1])
                    a = (inventory[index]-inventory[index+1])
                    ans += (index+1) * a * (inventory[index] + inventory[index] - a + 1) // 2
                    index += 1
                else:
                    a = orders//(index+1)
                    b = orders%(index+1)
                    ans += (index+1) * a * (inventory[index] + inventory[index] - a + 1) // 2 \
                           + b * (inventory[index] - a)
                    break

            else:
                a = orders//len(inventory)
                b = orders%len(inventory)
                ans += len(inventory)*a*(inventory[index]+inventory[index]-a+1)//2 \
                + b*(inventory[index]-a)
                break
        return int(ans%(10**9+7))