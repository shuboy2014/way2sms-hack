import urllib2
import cookielib
import getpass
import sys

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]


def login(username,password):
    if username and password:
        loginurl = "http://site24.way2sms.com/Login1.action?username=" + username + "&password=" + password
        r = opener.open(loginurl)
        jessionid = str(cj).split("~")[1].split(" ")[0]
        return jessionid
    else:
        return False

def sendSMS(sender_number,message,jessionid):
    messageurl = "http://site24.way2sms.com/smstoss.action?saction=s&Token="+jessionid+"&mobile=" + sender_number + "&message=" + message
    messageurl = '+'.join(messageurl.split(" "))
    try:
        r = opener.open(messageurl)
        print "Voila ! your message sended successfuly :) "
        sys.exit()
    except Exception as e:
        print e

if __name__ == '__main__':
    username = raw_input("Enter your Username : ")
    password = getpass.getpass("Enter your Password : ")
    jsessionid = login(username,password)
    if jsessionid:
        print "Login Successfully!"
        sender_number = raw_input("Enter Sender Number : ")
        while True:
            message = raw_input("Enter Message : ")
            if len(message) > 140 :
                print "Message length exceed 140 words ! type again"
            else:
                break
        message = "+".join(message.split())
        sendSMS(sender_number,message,jsessionid)
    else:
        "Oops ! Wrong Creditionals!"
        
