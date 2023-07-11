from setuptools import find_packages,setup

HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    '''
    This function will return list of requirements
    '''
    req = []
    with open(file_path) as file:
        req = file.readlines()
        req = [r.replace('\n',"") for r in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
    return req
setup(
    name='mlproject',
    version='0.0.1',
    author='Prasad',
    author_email='chaskarprasad200@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
