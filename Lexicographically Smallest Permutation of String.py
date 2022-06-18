n= int(input())
if n!=0:
    str = input()
else:
    print("")
    
def lex_smallest_permutation(n,str):
    return ''.join(sorted(str))

print(lex_smallest_permutation(n,str))
