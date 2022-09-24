class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        bags = [0 for i in range(num_people)]
        i = 1
        while candies > 0:
            bag_number = ((i - 1) % num_people)
            if candies < i:
                bags[bag_number] += candies
                candies = 0
            else:
                bags[bag_number] += i
                candies -= i
            i += 1
        return bags
            
