import math
import sys
import argparse


def get_input():
    """
    :return: using argparse, getting user input via cli and retuning all values
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', action='store', help="--type=[diff] | [annuity]")
    parser.add_argument('-c', '--principal', action='store', help="Total credit principal", default=None, type=int)
    parser.add_argument('-p', '--payment', action='store', help="Total payment", default=None, type=int)
    parser.add_argument('-P', '--periods', action='store', help="Period in months", default=None, type=int)
    parser.add_argument('-i', '--interest', action='store', help="Interest", default=None, type=float)
    args = parser.parse_args()

    if len(sys.argv) < 4 or args.interest is None:
        print("Incorrect parameters")
        exit(1)
    elif args.type not in ['diff', 'annuity'] or args.interest is None:
        print("Incorrect parameters")
        exit(1)
    return args.type, args.principal, args.payment, args.periods, args.interest


def validate_input(calculation, c_principal, payment, periods, interest):
    if calculation == 'diff' and c_principal and periods and interest:
        if c_principal < 0 or periods < 0 or interest < 0:
            print("Incorrect parameters")
            exit(2)
        else:
            diff_payment(c_principal, periods, interest)

    elif calculation == 'annuity' and c_principal and periods and interest:
        if c_principal < 0 or periods < 0 or interest < 0:
            print("Incorrect parameters")
            exit(2)
        else:
            annuity_payment(c_principal, periods, interest)

    elif calculation == 'annuity' and payment and periods and interest:
        if payment < 0 or periods < 0 or interest < 0:
            print("Incorrect parameters")
            exit(2)
        else:
            credit_principal(payment, periods, interest)

    elif calculation == 'annuity' and c_principal and payment and interest:
        if c_principal < 0 or payment < 0 or interest < 0:
            print("Incorrect parameters")
            exit(2)
        else:
            calculate_period(c_principal, payment, interest)

    else:
        print("Incorrect parameters")
        exit(2)


def calculate_period(_principal_, _payment_, _interest_):
    nominal_interest = _interest_ / (12 * 100)
    months = math.ceil(
        math.log(_payment_ / (_payment_ - nominal_interest * _principal_), 1 + nominal_interest))

    if months < 12:
        print(f"You need {int(months)} months to repay this credit!")
    elif months == 12:
        print(f"You need 1 year")
    elif months % 12 == 0:
        print(f"You need {int(months / 12)} years to repay this credit!")
    else:
        print(f"You need {months // 12} years and {months % 12} months to repay this credit!")
    print(f"Overpayment = {round((_payment_ * months) - _principal_)}")


def credit_principal(_payment_, _period_, _interest_):
    nominal_interest = _interest_ / (12 * 100)

    calc = nominal_interest * ((1 + nominal_interest) ** _period_) / ((1 + nominal_interest) ** _period_ - 1)
    credit_principal_ = math.floor(_payment_ / calc)

    print(f"Your credit principal = {credit_principal_}!\nOverpayment = {(_payment_ * _period_) - credit_principal_} ")


def annuity_payment(_principal_, _period_, _interest_):
    nominal_interest = _interest_ / (12 * 100)

    annuity_payment = math.ceil(_principal_ * (nominal_interest * ((1 + nominal_interest) ** _period_)) / (
            ((1 + nominal_interest) ** _period_) - 1))
    print(f"your annuity payment = {annuity_payment}!\nOverpayment = {(annuity_payment * _period_) - _principal_} ")


def diff_payment(_principal_, _period_, _interest_):
    nominal_interest = _interest_ / (12 * 100)
    monthly_payment = 0
    for m in range(1, _period_ + 1):
        diff = math.ceil(
            (_principal_ / _period_) + nominal_interest * (_principal_ - (_principal_ * (m - 1)) / _period_))
        print(f"Month {m}: paid out {diff}")
        monthly_payment += diff
    print(f"\nOverpayment = {monthly_payment - _principal_}")


def Main():
    """
    The main function of my program
    """
    calculation, c_principal, payment, periods, interest = get_input()
    validate_input(calculation, c_principal, payment, periods, interest)


if __name__ == '__main__':
    Main()
