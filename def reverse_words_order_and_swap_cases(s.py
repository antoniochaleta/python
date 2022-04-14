
def reverse_words_order_and_swap_cases(sentence):
    i=0
    sent=""
    
    while i != len(sentence):        
        temp=""
        if sentence[i].isupper():
            temp=sentence[i]
            sent+=temp.lower()
        else: 
            temp=sentence[i]
            sent+=temp.upper()
        i+=1
    print(sent)


reverse_words_order_and_swap_cases("aWESOME is cODING")