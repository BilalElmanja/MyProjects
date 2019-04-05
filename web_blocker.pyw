
import datetime as dt

hosts = open(r'C:\Windows\System32\Drivers\etc\hosts' , 'r+')
hosts.seek()
now_time = dt.datetime.now()
execute_time = dt.time(7 , 10 , 23)
blocked_websites = ['www.facebook.com' , 'www.instagram.com']
redirection = '0.0.0.0 '
hosts_content = hosts.readlines()
hosts_content = [lambda i : i[:-3] for i in hosts_content]
while True:
    if ( now_time.minute - execute_time.minute ) > 4:
        execute_time = now_time
        now_time = dt.datetime.now()
        if now_time.hour < 16:
            condition1 = True
            while condition1:
                for site in blocked_websites:
                    if site in hosts_content:
                        continue
                    else:
                        hosts.write('\n{} {}'.format(redirection , site))
                condition1 = False
            
        else:
            condition2 = True
            if (hosts_content[-1][8:-1] in blocked_websites):
                hosts_content.pop()
                continue
            else:
                condition2 = False
                continue
            

        






