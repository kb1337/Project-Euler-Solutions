number = ""
for i in range(1, 1000000):
    number += str(i)

result = (
    int(number[0])
    * int(number[9])
    * int(number[99])
    * int(number[999])
    * int(number[9999])
    * int(number[99999])
    * int(number[999999])
)

print(result)
