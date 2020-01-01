import easygui
#flavor=easygui.choicebox("what is your flavor?",choices=['aaa','bbb','ccc'])
#flavor=easygui.buttonbox("what is your flavor?",choices=['aaa','bbb','ccc'])
#flavor=easygui.enterbox("what is your flavor?")
flavor=easygui.enterbox("what is your flavor?",default='1234')
easygui.msgbox("your flavor is "+flavor)