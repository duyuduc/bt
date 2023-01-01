zoo=['tiger','bear','elephant','ant','mouse','fish','cat','wolf','sea dog','ant','goat','pikachu']
print('Danh sách các con thú trong sở thú là',zoo)
print('số lượng các con thú trong sở thú là',len(zoo))
find=input('Nhập con thú cần tìm trong sở thú:')
check= find in zoo
if check:
    print(find,'có trong sở thú')
else:
    print(find,'không có trong sở thú')