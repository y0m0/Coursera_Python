text = "X-DSPAM-Confidence:    0.8475"
start = text.find(':')
print float(text[start+1:])

#shorter  version
print float(text[text.find(':') + 1 :])