def peak_count(heights):
    peak_count = 0
    for i in range(1, len(heights)-1):
        if heights[i] > heights[i-1] and heights[i] > heights[i+1]:
            peak_count+=1
    return peak_count
    

t = int(input())
for i in range(1, t + 1):
  input() # dont care
  heights = [int(s) for s in input().split(" ")]
  print("Case #{}: {}".format(i, peak_count(heights)))