def get_position(p, h):
    return next((p.index(i) + 1 for i in p if i < h), len(p) + 1)


ppl = map(int, input().split())
height = int(input())
print(get_position(sorted(ppl, reverse=True), height))
