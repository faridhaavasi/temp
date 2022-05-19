def getPrefixSuffix(a, b, l):
	prefix = a[: l]
	lb = len(b)
	suffix = b[lb - l:]

	return (prefix + suffix)

a = 'test'
b = 'sti'
l = 4
print(getPrefixSuffix(a, b, l))




