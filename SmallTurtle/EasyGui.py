# encoding=gbk
# 图形用户界面模块
import easygui as eg
# eg.msgbox('欢迎光临','nice to meet you')
# eg.ynbox('我可以继续嘛','yolo',('confirm','cancel'))
# eg.buttonbox('点击你最爱的','doudou',('巧克力','糖果'))
# img = 'down.jpg'
# msg = 'Do you like the picture'
# choices = ['yes','no','keep option']
# reply = eg.buttonbox(msg,image=img,choices=choices)

msg = "Enter your personal information"
title = "Credit Card Application"
fieldNames = ["Name","Street Address","City","State","ZipCode"]
fieldValues = []  # we start with blanks for the values
fieldValues = eg.multenterbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = eg.multenterbox(errmsg, title, fieldNames, fieldValues)
print ("Reply was:", fieldValues)