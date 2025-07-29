grades = [70,50,60,90,86,53,20]

fail_sum = 0
fail_count = 0 
pass_sum = 0
pass_count = 0


for grade in grades:
    if grade >= 50:
        pass_sum += grade
        pass_count += 1
        continue

    fail_sum += grade
    fail_count += 1

    

    if fail_count > 0:
        avarege_fail = fail_sum / fail_count 
        print(f"ჩაჭრილი სტუდენტების საშუალო ქულა: {avarege_fail}" )
    else:
        print("არცერთი სტუდენტი არ ჩაიჭრილა")

    if pass_count > 0:
        avarege_pass = pass_sum / pass_count
        print(f"ჩაბარებული  სტუდენტაბის ქულა:{avarege_pass}")
    else:
        print("ჩაბარებული სტუდენტები არ არიან")

    if grade > 100:
        print("you ar alien")



