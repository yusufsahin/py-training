import re

pattern=r"\d+" #Bir veya daha fazla rakamı eşler

#derleme/compile
p=re.compile(pattern)

match=re.match(pattern,"123abc")

if match:
    print(match.group())

search=re.search(pattern,"abc123def")

if search:
    print(search.group())

matches=re.findall(pattern,"abc123def456ghi789")
print(matches)
matches2=re.findall(r"\D+","abc123def456ghi789")
print(matches2)

for match in re.finditer(r"\d+","abc123def456ghi789"):
    print(match.group())


for match in re.finditer(r"\D+","abc123def456ghi789"):
    print(match.group())

#re.sub(pattern, replacement, text)

result=re.sub(r"\d+","#","abc123def456")
print(result)

pattern2=re.compile(r"cat|dog")
match3=pattern2.search("I have a cat and dog.")
print(match3.group())

match3_1=pattern2.findall("I have a cat and dog.")
print(match3_1)

pattern2_1 = re.compile(r"(?=.*cat)(?=.*dog)")
if pattern2_1.search("I have a cat and dog."):
    print("cat ve dog var")
else:
    print("ikisi birden yok")

#Çapa / Anchor dizgedeki konumu eşler ^ ve $
pattern3= re.compile(r"^hello")
match4=pattern3.match("hello world")
if match4:
    print(match4.group())

pattern4=re.compile(r"world$")
match5=pattern4.search("hello world")
if match5:
    print(match5.group())


#Açgözlü ve Açgözsüz: #Tekrarlayıcılar varsayılan olarak açgözlüdür,
# yani mümkün olan en fazla karakteri eşler.
# #Tekrarlayıcıları açgözsüz yapmak için ? ekleyin
# (yani mümkün olan en az karakteri eşler).

greedy_pattern=re.compile(r"<.*>")
non_greedy_pattern=re.compile(r"<.*?>")
text="<div>hello</div>"
greedy_match=greedy_pattern.search(text)
print(greedy_match.group())
non_greedy_match=non_greedy_pattern.search(text)
print(non_greedy_match.group())

pattern8 = re.compile(r"(hello) (world) (python)")
match9 = pattern8.search("hello world python")
print(match9.group(0))
print(match9.group(1))
print(match9.group(2))
print(match9.group(3))


#Geriye dönük referanslar \number
pattern9 = re.compile(r"(\b\w+)\s+\1")
match10 = pattern9.search("hello hello world")

if match10:
    print(match10.group())
else:
    print("pattern9 eşleşme bulamadı")

pattern10 = re.compile(r"(\b\w+\s+\w+)\s+\1")

match11 = pattern10.search("hello world hello world")

if match11:
    print(match11.group())

#Global Eşleştirme
#Tüm eşleştirmeleri bulma

pattern10= re.compile(r"\b\w+\b")
matches3=pattern10.findall("hello world")
print(matches3)

for match in pattern10.finditer("hello world"):
    print(match.group())
