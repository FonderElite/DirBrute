import requests,argparse,threading
parser = argparse.ArgumentParser(description="BruteForce Directory")
parser.add_argument('-u','--url',metavar='',help="URL")
parser.add_argument('-w',"--wordlist",metavar='',help="Wordlist")
args = parser.parse_args()
class Request:
 def __init__(self,url,wordlist):
  self.url = url
  self.wordlist = wordlist
 def test_url(self):
  r = requests.get(self.url)
  print(r)
  if r.status_code != 400 and r.status_code < 400:
   print("Great host is up!")
   w = open(self.wordlist)
   for i in w:
    req = requests.get(self.url + "/" + self.wordlist)
    if req.status_code == 200 or req.status_code < 399:
     print("Success=>" + self.url + "/" + i)
    else:
     print(req.status_code)
     print("Fail=>" + "/" + i)
 def get_cookie(self):
  request = requests.get(self.url)
  a_session = requests.Session()
  a_session.get(self.url)
  session_cookies = a_session.cookies
  cookies_dictionary = session_cookies.get_dict()
  if request.status_code != 400 and request.status_code < 400:
   print(cookies_dictionary)
if __name__ == "__main__":
 classreq = Request(args.url,args.wordlist)
 info = classreq.get_cookie()
 classreq.test_url() 
