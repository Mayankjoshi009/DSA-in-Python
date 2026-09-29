#recusion


#head recursion

# count=0
# def func():
#     global count
#     if count==4:
#         return
#     print("mayank")
#     count += 1
#     func()       
# func()


#tail recursion

count=0
def func():
    global count
    if count==4:
        return
    count += 1
    func()
    print("mayank")
func()    