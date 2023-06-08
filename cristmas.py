with open("CrismasCards/employees.txt", "r") as file:
    names = file.read().splitlines()

with open("CrismasCards/template.txt", "r") as file:
    template_content = file.read()

for name in names:
    personalized_template = template_content.replace("NAME", name)

    with open(f"CrismasCards/cristmascards/{name}.txt", "w") as file:
        file.write(personalized_template)
