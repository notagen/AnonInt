def dictAccess():
    id = {}
    with open("template.txt") as f:
        # f_content = f.readline()
        for line in f:
            s1 = line.split(":")
            s2 = s1[1].split(",")
            # print(s2, end="")
            id[s1[0]] = s2
            # print(id)
    return id

"""
def newTemplate(name, value):
    with open("template.txt", "a") as f:
        f.write("\n")
        f.write(name + ":" + value)
    return 0
"""

def newTemplate2(name, list):
    with open("template.txt", "a") as f:
        f.write("\n")
        f.write(name + ":")
        for l in list:
            f.write(l + ",")
        f.truncate(f.tell()-1)
    return 0




# newTemplate("new", "ho,ho2")
# id2 = dictAccess()
# print(id2)

"""
id = {"abc": ["abc"]}
with open("templates.txt") as f:
    # f_content = f.readline()
    for line in f:
        s1 = line.split(":")
        s2 = s1[1].split(",")
        # print(s2, end="")
        id[s1[0]] = s2
        print(id)

with open("templates.txt", "a") as f:
    f.write("\n")
    f.write(id["abc"][0] + ":")
"""
