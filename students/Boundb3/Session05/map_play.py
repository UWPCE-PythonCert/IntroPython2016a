
#map play

l = [5,10,15,20]

fx = lambda x: 2*x

res = map(fx,l)

for x in res:
    print(x)

d={"spring":("happy yellow", "bright pink")}
  # "midnight" : ("dark blue", "shadow black"),
   #"neon" : ("electric orange", "blinding silver")}

#fx2 = lambda args: "{} and {} make good colors".format(enumerate(args))
fx2 = lambda args: "{} and {} make good colors".format(args["spring"][0],args["spring"][1])
print(fx2(d))
