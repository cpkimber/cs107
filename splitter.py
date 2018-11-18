a = "set server us\n set locale us\n set lang eng"

settings = []
l_index = 0
while a.find("\n", l_index) != -1:
    r_index = a.find("\n", l_index)
    settings.append(a[l_index:r_index])
    l_index = r_index + 1
settings.append(a[l_index:])


print(settings)


for s in settings:
  l_index = 0
  subsetting = []
  while " " in s:

    subsetting.append()
