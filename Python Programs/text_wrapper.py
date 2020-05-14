import textwrap
# basically used to convert sentence into fixed length of paragraphs.
s = input('Enter str: ')
w = int(input('Enter width: '))
lst = textwrap.TextWrapper(width=w)
lst1 = lst.wrap(text=s)
print(lst1)

