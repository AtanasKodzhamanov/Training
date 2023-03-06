input = [4, -7, 2, 5, -9, 3, 1, 2]


def func(input):
    max = 0
    left = 0
    right = 0
    maxsum = 0
    cursum = 0
    for right in range(0, len(input)):

        cursum += input[right]

        if cursum >= maxsum:
            maxsum = cursum
        if cursum <= 0:
            cursum = 0
            left = right+1

    return max


func(input)
