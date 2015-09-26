from pyquery import PyQuery as pq
from requests import get

repPage = "http://ziplook.house.gov/htbin/findrep?ZIP={}&Submit=FIND+YOUR+REP+BY+ZIP"
senPage = "http://www.senate.gov/senators/contact/senators_cfm.cfm?State={}"

def printCong(address):
	zipCode = address[-5:]
	state = address[-8:][:2]
	reps = []
	sens = []
	realsens = []
	result = get(repPage.format(zipCode))
	content = pq(result.content)
	name = content("#PossibleReps")
	rep = name.find("a")
	for r in rep:
		if r.text != None:
			reps.append(r.text)
	senRes = get(senPage.format(state))
	senContent = pq(senRes.content)
	senNames = senContent(".contenttext")
	sen = senNames.find("a")
	for s in sen:
		if s.text != None:
			temptext = ""
			for i in s.text:
				if i == "\n":
					break
				temptext+=i
			sens.append(temptext)
	realsens.append(sens[2])
	realsens.append(sens[4])
	print "Senators for {}:".format(address)
	print realsens[0]
	print realsens[1] + "\n"
	print "Representatives for {}:".format(address)
	for r in reps:
		print r
	print "\n"
adds = []
adds.append("46855 Lyndon Ave, Canton, MI 48187")
adds.append("123 Winter St, Waltham, MA 02451")
adds.append("22362 Cupertino Rd, Cupertino, CA 95014")
adds.append("6510 SE Lake Cir Dr, Stuart, FL 34997")
adds.append("601 E 3rd St, Austin, TX 78701")

for a in adds:
	printCong(a)