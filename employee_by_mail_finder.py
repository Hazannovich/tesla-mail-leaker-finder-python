
number_of_double_spaces = 0
with open('./leaked_mail.txt', 'r') as leaked_mail:
    leaked_mail_lines = leaked_mail.readlines()
    for line in leaked_mail_lines:
        number_of_double_spaces += line.count('  ')

with open('./mesla-mailing-list.txt', 'r') as mails_list:
    employees_mails = mails_list.readlines()
    print(f"{employees_mails[number_of_double_spaces-1]} is the leaker!!!")
