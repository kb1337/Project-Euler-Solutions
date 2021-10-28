# 1 times 200 pence,
# 2 time 100 pence,
# 4 times 50 pence,
# 10 times 20 pence,
# 20 times 10 pence,
# 40 times 5 pence,
# 100 times 2 pence,
# 200 times 1 pence

count = 8

for c1 in range(200):
    for c2 in range(100):
        for c5 in range(40):
            for c10 in range(20):
                for c20 in range(10):
                    for c50 in range(4):
                        for c100 in range(2):
                            total = (
                                c1 * 1
                                + c2 * 2
                                + c5 * 5
                                + c10 * 10
                                + c20 * 20
                                + c50 * 50
                                + c100 * 100
                            )

                            if total == 200:
                                count += 1

print(count)
