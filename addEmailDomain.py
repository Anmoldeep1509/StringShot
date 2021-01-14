def addDomain(ip_list, domainName):
	# output list having the final emails
	op_list = list()
	for item in ip_list:
		item = item.strip() + domainName
		op_list.append(item)

	return op_list
