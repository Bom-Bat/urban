def send_email(message, recipient, *, sender='university.help@gmail.com'):
    print(f'\n\tТекст письма: \n\t{message}')
    a = '@' in recipient and recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')
    b = '@' in sender and sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')
    if not a or not b:
        print(f'\n\tНевозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print(f'\n\tНельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'\n\tПисьмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'\n\tНЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')


print(f'\n\tВведите пожайлуста следущее')
mess = input(f'\n\tТекст сообщения: ')
rec = input(f'\n\tАдрес получателя: ')
send = input(f'\n\tАдрес отправителя (0 если не меняется): ')
if send == '0':
    send_email(mess, rec)
else:
    send_email(mess, rec, sender=send)
