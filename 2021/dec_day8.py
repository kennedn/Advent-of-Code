with open('day_8.txt', 'r') as f:
    input = [[a.strip().split(' | ')[0].split(' '), a.strip().split(' | ')[1].split(' ')] for a in f]

def getoutput(i):
    nums = ['0','1','2','3','4','5','6','7','8','9']
    nums[1] = [a for a in i[0] if len(a) == 2][0]
    nums[4] = [a for a in i[0] if len(a) == 4][0]
    nums[7] = [a for a in i[0] if len(a) == 3][0]
    nums[8] = [a for a in i[0] if len(a) == 7][0]
    nums[9] = [a for a in i[0] if len(a) == 6 and set(nums[4]).issubset(set(a))][0]
    nums[0] = [a for a in i[0] if len(a) == 6 and set(nums[1]).issubset(set(a)) and a not in nums][0]
    nums[6] = [a for a in i[0] if len(a) == 6 and a not in nums][0]
    nums[3] = [a for a in i[0] if len(a) == 5 and set(nums[1]).issubset(set(a))][0]
    nums[5] = [a for a in i[0] if len(a) == 5 and (set(nums[4]) - set(nums[1])).issubset(set(a)) and a not in nums][0]
    nums[2] = [a for a in i[0] if len(a) == 5 and a not in nums][0]

    return int(''.join([str(nums.index([n for n in nums if set(n) == set(a)][0])) for a in i[1]]))

print(f'Part B: total output sum value - {sum([getoutput(a) for a in input])}')