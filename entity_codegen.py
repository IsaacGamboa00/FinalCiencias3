"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm
import subprocess


def main(debug=False):

    this_folder = dirname(__file__)

    #subprocess.call([this_folder+"/initProject.bat"])
    subprocess.call([this_folder+"/createFolders.bat"])

    entity_mm = get_entity_mm(debug)

    person_model = entity_mm.model_from_file(join(this_folder, 'person.ent'))



    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in person_model.entities:
            return True
        else:
            return False

    srcgen_folder = join(this_folder, 'FinalProject/src/app')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)


    jinja_env.tests['entity'] = is_entity

    template = jinja_env.get_template('list.template')
    auxEntity = person_model.entities[0]
    with open(join(srcgen_folder+"/components",
        "%s.component.html" % auxEntity.name.capitalize()), 'w') as f:
        f.write(template.render(entity=auxEntity))

    template = jinja_env.get_template('style.template')

    with open(join(srcgen_folder+"/components",
        "%s.component.scss" % auxEntity.name.capitalize()), 'w') as f:
        f.write(template.render(entity=auxEntity))

    template = jinja_env.get_template('logic.template')

    with open(join(srcgen_folder+"/components",
        "%s.component.ts" % auxEntity.name.capitalize()), 'w') as f:
        f.write(template.render(entity=auxEntity))  

    template = jinja_env.get_template('module.template')

    with open(join(srcgen_folder,
        "app.module.ts"), 'w') as f:
        f.write(template.render(entity=auxEntity)) 

    template = jinja_env.get_template('app.template')

    with open(join(srcgen_folder,
        "app.component.html"), 'w') as f:
        f.write(template.render(entity=auxEntity))  

    template = jinja_env.get_template('interface.template')

    for entity in person_model.entities:
        with open(join(srcgen_folder+"/model",
                       "%s.ts" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))



if __name__ == "__main__":
    main()
