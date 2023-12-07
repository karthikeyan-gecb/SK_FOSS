def max_area(height):
    max_water = 0
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        container_height = min(height[left], height[right])
        current_water = width * container_height
        max_water = max(max_water, current_water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Example usage:
height = eval(input("Enter the list :"))
result = max_area(height)
print(result)
#sample output
''''
Enter the list :[1,8,6,2,5,4,8,3,7]
49
'''