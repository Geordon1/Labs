
def find_common_participants (first_group, second_group, separator = ","):
    g1 = first_group.split(separator)
    g2 = second_group.split(separator)
    a = []
    for i in range(len(g1)):
        for j in range(len(g2)):
            if g1[i] == g2[j]:
                a.append(g1[i])
    return a

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants (participants_first_group, participants_second_group, "|")

print(result)
