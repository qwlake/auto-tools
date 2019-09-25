import os

NAME_DIAGRAM = "sequence"   # 다이어그램 이름
NUM_TRASH_LINE = 4          # 문서 사이의 trash 라인 수

# 문서 사이의 trash 라인들 제거
trash_sliced = []
if not(os.path.isdir("data")):
    os.makedirs(os.path.join("data"))
try:
    with open('data/' + NAME_DIAGRAM + '_trash_sliced.txt', 'r', encoding='utf-8') as f:
        trash_sliced = f.readlines()
except:
    with open('data/' + NAME_DIAGRAM + '.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        count = NUM_TRASH_LINE
        for i, line in enumerate(lines):
            if count is not NUM_TRASH_LINE or "PlantUML 언어참조가이드" in line:
                count -= 1
                if count == 0:
                    count = NUM_TRASH_LINE
            else:
                trash_sliced.append(line)
    with open('data/' + NAME_DIAGRAM + '_trash_sliced.txt', 'w', encoding='utf-8') as f:
        f.writelines(trash_sliced)

# 다이어그램별로 파일로 저장
flag = False
uml_lines = []
umls_dic = {}
uml_count = 1
univ_lines = []
for line in trash_sliced:
    if "@startuml" in line:
        flag = True
        uml_lines.append(line)
        univ_lines.append(line)
    elif "@enduml" in line:
        flag = False
        uml_lines.append(line)
        univ_lines.append(line)
        univ_lines.append('\n')
        umls_dic[uml_count] = uml_lines
        uml_count += 1
        uml_lines = []
    elif flag:
        uml_lines.append(line)
        univ_lines.append(line)
if not os.path.isdir("output"):
    os.makedirs(os.path.join("output"))
if not os.path.isdir("output/"+NAME_DIAGRAM):
    os.makedirs(os.path.join("output/"+NAME_DIAGRAM))
with open("output/" + NAME_DIAGRAM + "/univ.txt", 'w', encoding='utf-8') as f:
    f.writelines(univ_lines)
for num, uml in umls_dic.items():
    with open("output/" + NAME_DIAGRAM + "/uml" + str(num).zfill(2), 'w', encoding='utf-8') as f:
        f.writelines(uml)