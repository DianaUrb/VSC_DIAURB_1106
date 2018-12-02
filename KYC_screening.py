
import os
import wx
import datetime
import sqlite3

from datetime import timedelta
year = timedelta(days=365)


client_data={
    'name':'John',
    'surname':'Smith',
    #name and surname as stated in international ID document
    'date_of_birth':'05 12 1980',
    #date of birth format dd/mm/yyyy
    'country_of_origin':['Vanuatu'],
    #country of origin must be submitted using official country name
    'country_of_residence':['Haiti'],
    #country of residence must be submitted using official country name
    'address':'Any address',
    #address format must be predefined in questionnaire
    'passportNo':'12345678',
    'occupation_field':['Any'],
    #occupation choice must be limited in questionnaire
    'income_type':['Dividend'],
    'turnover_month':['<1000 EUR'],
    'transaction_number_month':['<5'],
    #Limit input format!
    'PEP':['N/A']
    #for PEPs it's PEP or N/A
}


def screen_countries(client_data):
    f_risk_score1=0
    aml_drawbacks_list = open('AML_drawbacks', 'r')
    full_country_list = client_data['country_of_origin']
    for x in client_data['country_of_residence']:
        full_country_list.append(x)
    # full_country_list.append(client_data['country_of_residence'])
    for country in aml_drawbacks_list.readlines():
        country=country[:-1]
        for val in full_country_list:
            if val == country:
                f_risk_score1 = 20
            else:
                pass
    print ('Risk score 1: ')
    print f_risk_score1
    return f_risk_score1


screen_countries(client_data)


def screen_corruption(client_data):
    f_risk_score2 = 0
    corruption_list=open('Corruption_criminal','r')
    full_country_list = client_data['country_of_origin']
    for x in client_data['country_of_residence']:
        full_country_list.append(x)
    for country in corruption_list.readlines():
        country=country[:-1]
        for val in full_country_list:
            if val == country:
                 f_risk_score2 = 20
            else:
                pass
    print ('Risk score 2: ')
    print f_risk_score2
    return f_risk_score2


screen_corruption(client_data)


def screen_offshore(client_data):
    f_risk_score3 = 0
    offshore_list=open('Offshore','r')
    full_country_list = client_data['country_of_origin']
    for x in client_data['country_of_residence']:
        full_country_list.append(x)
    for country in offshore_list.readlines():
        country=country[:-1]
        for val in full_country_list:
            if val == country:
                f_risk_score3 = 20
            else:
                pass
    print ('Risk score 3: ')
    print f_risk_score3
    return f_risk_score3


screen_offshore(client_data)


def screen_sanctions(client_data):
    f_risk_score4 = 0
    sanctions_list=open('Sanctions','r')
    full_country_list = client_data['country_of_origin']
    for x in client_data['country_of_residence']:
        full_country_list.append(x)
    for country in sanctions_list.readlines():
        country=country[:-1]
        for val in full_country_list:
            if val == country:
                f_risk_score4 = 20
            else:
                pass
    print ('Risk score 4: ')
    print f_risk_score4
    return f_risk_score4


screen_sanctions(client_data)


def screen_terroristact(client_data):
    f_risk_score5 = 0
    terroristact_list=open('Terrorist_activity','r')
    full_country_list = client_data['country_of_origin']
    for x in client_data['country_of_residence']:
        full_country_list.append(x)
    for country in terroristact_list.readlines():
        country=country[:-1]
        for val in full_country_list:
            if val == country:
                f_risk_score5 = 20
            else:
                pass
    print ('Risk score 5: ')
    print f_risk_score5
    return f_risk_score5


screen_terroristact(client_data)


def screen_high_risk(client_data):
    f_risk_score6 = 0
    high_risk_list = open('High_risk_criteria','r')
    for positive_match in high_risk_list.readlines():
        positive_match=positive_match.replace("\n", "")
        for val in client_data['PEP']:
            if val == positive_match:
               f_risk_score6 = 20
            else:
                pass
    print ('Risk score 6: ')
    print f_risk_score6
    return f_risk_score6


screen_high_risk(client_data)


def screen_occupation(client_data):
    f_risk_score7 = 0
    occupation = ['Legal services', 'Electronic trading', 'Arms dealing', 'Cryptocurrency trading']
    for positive_match in occupation:
        for val in client_data['occupation_field']:
            if val == positive_match:
                f_risk_score7 = 20
            else:
                pass
    print ('Risk score 7: ')
    print f_risk_score7
    return f_risk_score7


screen_occupation(client_data)


def screen_income_type(client_data):
    f_risk_score8 = 0
    income_type=['Individual business', 'Dividend', 'Crypto trading']
    for positive_match in income_type:
        for val in client_data['income_type']:
            if val == positive_match:
                f_risk_score8 = 20
            else:
                pass
    print ('Risk score 8: ')
    print f_risk_score8
    return f_risk_score8


screen_income_type(client_data)


def screen_turnover_month(client_data):
    f_risk_score9 = 0
    turnover_month=['5000-15 000 EUR','15 000-30 000 EUR','>30 000 EUR']
    for positive_match in turnover_month:
        for val in client_data['turnover_month']:
            if val == positive_match:
                f_risk_score9 = 20
            else:
                pass
    print ('Risk score 9: ')
    print f_risk_score9
    return f_risk_score9


screen_turnover_month(client_data)


def screen_transaction_number_month(client_data):
    f_risk_score10 = 0
    transaction_number_month=['10-20','20-30']
    for positive_match in transaction_number_month:
        for val in client_data['transaction_number_month']:
            if val == positive_match:
                f_risk_score10 = 20
            else:
                pass
    print ('Risk score 10: ')
    print f_risk_score10
    return f_risk_score10


screen_transaction_number_month(client_data)


def assign_risk_group(final_score=''):
    f_risk_score1 = screen_countries(client_data)
    f_risk_score2 = screen_corruption(client_data)
    f_risk_score3 = screen_offshore(client_data)
    f_risk_score4 = screen_sanctions(client_data)
    f_risk_score5 = screen_terroristact(client_data)
    f_risk_score6 = screen_high_risk(client_data)
    f_risk_score7 = screen_occupation(client_data)
    f_risk_score8 = screen_income_type(client_data)
    f_risk_score9 = screen_turnover_month(client_data)
    f_risk_score10 = screen_transaction_number_month(client_data)

    #print f_risk_score1
    #print f_risk_score2
    #print f_risk_score3
    #print f_risk_score4
    #print f_risk_score5
    #print f_risk_score6
    #print f_risk_score7
    #print f_risk_score8
    #print f_risk_score9
    #print f_risk_score10

    final_score = (
            f_risk_score1 +
            f_risk_score2 +
            f_risk_score3 +
            f_risk_score4 +
            f_risk_score5 +
            f_risk_score6 +
            f_risk_score7 +
            f_risk_score8 +
            f_risk_score9 +
            f_risk_score10)

    print ('FINAL SCORE IS: ')
    print final_score

    global risk_group

    if f_risk_score1 > 0 or f_risk_score2 > 0 or f_risk_score3 > 0 or f_risk_score4 > 0 or f_risk_score5 > 0:
        risk_group = 'Very high risk'
    elif f_risk_score6 > 0:
        risk_group = 'High risk'
    elif f_risk_score7 > 0:
        risk_group = 'Medium'
    else:
        if final_score < 40:
            risk_group = 'Very low risk'
        elif final_score >= 40 and final_score <80:
            risk_group = 'Low risk'
        elif final_score >= 80 and final_score <120:
            risk_group = 'Medium risk'
        elif final_score >= 120 and final_score <160:
            risk_group = 'High risk'
        else:
            risk_group = 'Very high risk'
    print risk_group

    #global next_risk_assessment
    #next_risk_assessment = datetime.datetime.now() + year

    if risk_group == 'Very low risk':
        deposit_limit = 1000
        withdraw_limit = 1000
        next_risk_assessment = datetime.datetime.now() + year
        next_risk_assessment.strftime('%Y-%m-%d')
        print (
            'Risk group: Very low risk:',
            ('Deposit limit ', deposit_limit, 'EUR'),
            ('Withdraw limit ', withdraw_limit, 'EUR'),
            ('Next risk assessment ', next_risk_assessment))

    elif risk_group == 'Low risk':
        deposit_limit = 1000
        withdraw_limit = 1000
        next_risk_assessment = datetime.datetime.now() + year
        next_risk_assessment.strftime('%Y-%m-%d')
        print (
            'Risk group: Low risk:',
            ('Deposit limit ', deposit_limit, 'EUR'),
            ('Withdraw limit ', withdraw_limit, 'EUR'),
            ('Next risk assessment ', next_risk_assessment))

    elif risk_group == 'Medium risk':
        deposit_limit = 1000
        withdraw_limit = 1000
        next_risk_assessment = datetime.datetime.now() + year
        next_risk_assessment.strftime('%Y-%m-%d')
        print (
            'Risk group: Medium risk:',
            ('Deposit limit ', deposit_limit, 'EUR'),
            ('Withdraw limit ', withdraw_limit, 'EUR'),
            ('Next risk assessment ', next_risk_assessment))

    elif risk_group == 'High risk':
        deposit_limit = 1000
        withdraw_limit = 1000
        next_risk_assessment = datetime.datetime.now() + year
        next_risk_assessment.strftime('%Y-%m-%d')
        print (
            'Risk group: High risk:',
            ('Deposit limit ', deposit_limit, 'EUR'),
            ('Withdraw limit ', withdraw_limit, 'EUR'),
            ('Next risk assessment ', next_risk_assessment))

    else:
        print ('Risk group: Very high risk. Verification not possible')


assign_risk_group()


def commit_database():
    import sqlite3
    conn = sqlite3.connect('KYC.db')
    c = conn.cursor()
    client_name = client_data['name']
    client_surname = client_data['surname']
    eval_date = datetime.datetime.now().strftime('%Y-%m-%d')
    eval_result = risk_group
    next_eval_date = (datetime.datetime.now() + year).strftime('%Y-%m-%d')

    print 'Data in database'
    c.execute("""INSERT INTO kyc_table ('name', 'surname', 'eval_date', 'eval_result', 'next_eval_date')
                                        VALUES ('{}', '{}', '{}', '{}', '{}')
                            """.format(client_name, client_surname, eval_date, eval_result, next_eval_date))
    conn.commit()
    c.close


commit_database()