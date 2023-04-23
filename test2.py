args = 'text=搜索'


def a(args):
    if "=" in args:
       args =  args.split("=")
       print(args)
       print(args[1])

a(args)

b = "12312"
print(b)