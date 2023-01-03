

with open('./TOP-SECRET.txt', 'r') as original_mail:
    mail_lines = original_mail.readlines()

with open('./mesla-mailing-list.txt', 'r') as mails_list:
    employees_mails = mails_list.readlines()

number_of_spaces = 1
for employee_mail in employees_mails:
    employee_name = employee_mail.split('@')[0]
    current_number_of_spaces = 0
    with open(f'./unique_mail_for_each_employee/{employee_name}_{number_of_spaces}_spaces.txt', 'w') as unique_mail:
        for line in mail_lines:
            if number_of_spaces > current_number_of_spaces:
                for word in line.split():
                    if word != '\n' and not word.endswith('\n') and number_of_spaces > current_number_of_spaces:
                        unique_mail.write(f"{word}  ")
                        current_number_of_spaces += 1
                    else:
                        if word.endswith('\n'):
                            unique_mail.write(f"{word}")
                        else:
                            unique_mail.write(f"{word} ")
            else:
                unique_mail.write(line)
        number_of_spaces += 1
