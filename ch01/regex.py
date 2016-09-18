import re


result = re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
           '''
                sales@phptr.com
                postmaster@phptr.com
                eng@phptr.com
                noreply@phptr.com
                admin@phptr.com
           ''')
print(result)