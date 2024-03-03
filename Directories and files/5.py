color = ['Purple', 'Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('C:\PP\Test.txt', "w") as myfile:
        for i in color:
                myfile.write("%s\n" % i)

content = open('C:\PP\Test.txt')
print(content.read())