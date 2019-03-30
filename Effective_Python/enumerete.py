flavor_list = ['vanilla', '‘chocolate’', '‘pecan’', '‘strawberry’']
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))

for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))
