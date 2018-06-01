import os
file=('C:\\Users\\victo\\Desktop\\paragraph_2.txt')
lines =0
nwords =0
nsent=0
nchar=0
with open(file,'r') as f:
    for line in f:
        chars=line
        words=line.split()
        sents=line.splitlines()
        lines+=1
        nwords+=len(words)
        nsent+=len(sents)
        nchar+=len(chars)
        avg_let_ct=(nchar)/(nwords)
        avg_sent_len=(nwords)/(nsent)
print('Paragraph Analysis')
print('---------------------')
print("Approximate sentence count:",nsent)
print("Approximate Word Count:",nwords)
print("Average Letter Count:", float(avg_let_ct))
print("Average Sentence Length:", avg_sent_len)

#sets output file 
output_path = os.path.join('paragraphHW.txt')

# opens output file and writes to it
with open(output_path, 'w') as txtfile:

    txtfile.writelines('Paragraph Analysis\n-----------------\nApproximate Word Count: ' 
                        + str(nwords)+ '\nApproximate Sentence Count: '+ str(nsent) + 
                        '\nAverage Letter Count: ' + str(float(avg_let_ct)) + 
                        '\nAverage Sentence Length: ' + str(avg_sent_len))

# opens output file and prints to terminal
with open(output_path, 'r') as txtout:
    print(txtout.read())
