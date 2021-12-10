class Demo:
    def findMin(self, nums):
        min = nums[0]
        for num in nums:
            if (num < min):
                min = num
        return min

    def findMax(self, nums):
        max = nums[0]
        for num in nums:
            if (num > max):
                max = num
        return max

    def calculateAverage(self, nums):
        sum = 0
        for num in nums:
            sum += num
        average = sum / len(nums)
        return average
    
    def handleNumbers(self, nums):
        print("Max:", self.findMax(nums))
        print("Min:", self.findMin(nums))
        print("Average:", self.calculateAverage(nums))
