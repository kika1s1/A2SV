# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E

def calc(prefix, m, u, l):
    s = prefix[m + 1] - prefix[l - 1]
    return (s * (2 * u - s + 1)) / 2


def solve_case():
    n = int(input())
    nums = list(map(int, input().split()))

    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    answers = []

    q = int(input())
    for _ in range(q):
        l, u = map(int, input().split())

        left = l - 1
        right = n - 1
        ans = right

        while left <= right:
            mid = (left + right) // 2
            s = prefix[mid + 1] - prefix[l - 1]

            if s >= u:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        if ans > l - 1 and calc(prefix, ans - 1, u, l) >= calc(prefix, ans, u, l):
            ans -= 1

        answers.append(ans + 1)

    return answers


def main():
    t = int(input())

    for _ in range(t):
        answers = solve_case()
        print(*answers)


if __name__ == '__main__':
    main()