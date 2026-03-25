tech_name  = 'Power Bi'
sound = 'start'
print('1 current_tech tech_name = ', tech_name)

def current_tech():
    global tech_name
    global sound
    print('2 current_tech tech_name = ', tech_name)

    tech_name = 'Python'
    print('3 current_tech tech_name = ', tech_name)


current_tech()
print('4 current_tech tech_name = ', tech_name)
