def norm(phone):
    phone = phone.replace('-', '').replace('(', '').replace(')', '').replace('+', '')
    if phone.startswith('8'):
        phone = '7' + phone[1:]
    elif not phone.startswith('7'):
        phone = '7495' + phone
    return phone[:4] + phone[-7:]

new = norm(input().strip())
book = [norm(input().strip()) for _ in range(3)]

for saved in book:
    print("YES" if new == saved else "NO")
