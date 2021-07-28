ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_to_twenty = ['', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENCE = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def written_lenght(number):
    global ONES
    global ten_to_twenty
    global TENCE
    letters = ''

    if len(str(number)) == 1:
        letters = ONES[number]
        
    elif len(str(number)) == 2:
        if number <20:
            letters = ten_to_twenty[(number % 10) + 1]
        else:
            letters = TENCE[int(str(number)[0]) - 1] + ONES[int(str(number)[1])]

    elif len(str(number)) == 3:
        if int(str(number)[1]) == 0:
            if int(str(number)[2]) == 0:
                letters = ONES[int(str(number)[0])] + 'hundred'
            else:
                letters = ONES[int(str(number)[0])] + 'hundredand' + ONES[int(str(number)[2])]
        elif int(str(number)[1]) == 1:
            letters = ONES[int(str(number)[0])] + 'hundredand' + ten_to_twenty[int(str(number)[2]) + 1]
        else:
            letters = ONES[int(str(number)[0])] + 'hundredand' + TENCE[int(str(number)[1]) - 1] + ONES[int(str(number)[2])]
    else:
        letters = 'onethousand'
    #print("{:4} --> {:30} --> {:3}".format(str(number), letters, str(len(letters))))
    return len(letters)

sum = 0
for number in range(1, 1001):
    sum += written_lenght(number)
print(sum)
