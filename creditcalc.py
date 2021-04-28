import sys
import argparse
import math

parser = argparse.ArgumentParser(description="Financial calculator.")
parser.add_argument("--type", default=None)
parser.add_argument("--principal", default=None)
parser.add_argument("--interest", default=None)
parser.add_argument("--payments", default=None)
parser.add_argument("--periods", default=None)
args = parser.parse_args()
value_count = 0
neg_value = 0
check_list = []
value_list = []

if bool(args.type):
    value_count += 1
    check_list.append(1)
    value_list.append(args.type)
else:
    check_list.append(0)

if bool(args.principal):
    value_count += 1
    check_list.append(1)
    value_list.append(float(args.principal))
else:
    check_list.append(0)
    value_list.append(0)

if bool(args.interest):
    value_count += 1
    check_list.append(1)
    value_list.append(float(args.interest))
else:
    check_list.append(0)

if bool(args.payments):
    value_count += 1
    check_list.append(1)
    value_list.append(int(args.payments))
else:
    check_list.append(0)
    value_list.append(0)

if bool(args.periods):
    value_count += 1
    check_list.append(1)
    value_list.append(int(args.periods))
else:
    check_list.append(0)
    value_list.append(0)


if value_count != 4:
    print("Incorrect parameters")
elif args.type != "annuity" and args.type != "diff":
    print("Incorrect parameters")
elif args.type == "diff" and bool(check_list[3]):
    print("Incorrect parameters")
elif check_list[2] == 0:
    print("Incorrect parameters")

neg_value = sum(1 for value in check_list if value < 0)
if neg_value > 0:
    print("Incorrect parameters")

nom_inter = value_list[2] / (12 * 100)

if (value_list[0] == "diff" and check_list[1] != 0) and (check_list[4] !=0 and check_list[2] != 0):
    pay_value = []
    current_month = 1
    over_pay = 0
    for i in range (value_list[4]):
        diff_value = math.ceil((value_list[1] / value_list[4]) + nom_inter * (value_list[1] - ((value_list[1] * (current_month - 1)) / value_list[4])))
        pay_value.append(diff_value)
        print("Month " + str(current_month) + ": payment is " + str(diff_value))
        current_month += 1
        over_pay += diff_value - (value_list[1] / value_list[4])
    print()
    print("Overpayment = " + str(math.ceil(over_pay)))

elif (value_list[0] == "annuity" and check_list[1] != 0) and (check_list[4] !=0 and check_list[2] != 0):
    nom_inter = value_list[2] / (12 * 100)
    annuity = math.ceil(value_list[1] * ((nom_inter * (math.pow((1 + nom_inter), value_list[4]))) / (math.pow((1 + nom_inter), value_list[4]) - 1)))
    over_pay = (annuity * value_list[4]) - value_list[1]
    print("Your annuity payment = " + str(annuity)+"!")
    print("Overpayment: " + str(math.ceil(over_pay)))

elif (value_list[0] == "annuity" and check_list[3] != 0) and (check_list[4] !=0 and check_list[2] != 0):
    nom_inter = value_list[2] / (12 * 100)
    loan_ppal = math.floor(value_list[3] / ((nom_inter * (math.pow((1 + nom_inter), value_list[4]))) / (math.pow((1 + nom_inter), value_list[4]) - 1)))
    over_pay = (value_list[3] * value_list[4]) - loan_ppal
    print("Your Loan principal = " + str(loan_ppal) + "!")
    print("Overpayment: " + str(math.ceil(over_pay)))

elif (value_list[0] == "annuity" and check_list[1] != 0) and (check_list[3] !=0 and check_list[2] != 0):
    nom_inter = value_list[2] / (12 * 100)
    num_pay =  math.ceil(math.log(value_list[3] / (value_list[3] - nom_inter * value_list[1]), (1 + nom_inter)))

    if num_pay - math.floor(num_pay) > 0:
        round_month_payment = math.floor(num_pay) + 1
    elif num_pay - math.floor(num_pay) == 0:
        round_month_payment = num_pay

    if round_month_payment < 12:
        print("It will take " + str(round_month_payment) + " months to repay this loan!")
    elif round_month_payment % 12 == 0:
        print("It will take " + str(int(round_month_payment / 12)) + " years to repay this loan!")
    elif round_month_payment % 12 == 1:
        print("It will take " + str(round_month_payment // 12) + " years and " + str(round_month_payment % 12) + " month to repay this loan!")
    elif round_month_payment % 12 > 1:
        print("It will take " + str(round_month_payment // 12) + " years and " + str(round_month_payment % 12) + " months to repay this loan!")
    over_pay = (value_list[3] * num_pay) - value_list[1]
    print("Overpayment: " + str(math.ceil(over_pay)))