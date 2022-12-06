#!usr/bin/env python3
from docxtpl import DocxTemplate
import convertapi
import os
import os.path
import random
import shutil
import string


def copy_file(cert_id: str, example_n: str='example.docx') -> 'file':
    shutil.copy(example_n, cert_id)


def id_generator(size=8, chars=string.ascii_uppercase + string.digits) -> str:
    return (''.join(random.choice(chars) for _ in range(size)))


def example_changer(cert_id: str, name_surname: str, course_name: str, date: str, place: str, course_director: str) -> 'pdf':
    doc = DocxTemplate(cert_id)
    context = {'name_surname' : name_surname,
                'cert_id': cert_id[:len(cert_id)-5],
                'course_name': course_name,
                'date': date,
                'place': place,
                'course_director': course_director
            }
    doc.render(context)
    doc.save(cert_id)
    convertapi.api_secret = 'API'
    convertapi.convert('pdf', {
    'File': cert_id
    }, from_format = 'docx').save_files('PATH')
    try:
        os.remove(cert_id)
        print('[+] Removed .docx file, only pdf left')
    except:
        print('[-] An error happenned while deleting .docx file')
    


def run(id: int, name_surname: str, course_name: str, date: str, place: str, course_director: str):
    if os.path.isfile(f'{id}.pdf'):
        print('[+] File has been created before you asked.')
    else:
        print(f'[-] Generating file. {id}: {name_surname}')
        cert_id = str(id) + '.docx'
        copy_file(cert_id)
        example_changer(cert_id, name_surname, course_name, date, place, course_director)


if __name__ == '__main__':
    run(id_generator(), 'a','a','a','a','a')