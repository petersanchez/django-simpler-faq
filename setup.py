import os
from distutils.core import setup


project_name = 'simpler_faq'
long_description = open('README.rst').read()

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk(project_name):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.') or dirname == '__pycache__':
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[(len(project_name) + 1):]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name='django-simpler-faq',
    version=__import__(project_name).get_version(),
    package_dir={project_name: project_name},
    packages=packages,
    package_data={project_name: data_files},
    description='Django app to generate an absolute basic FAQ page.',
    author='Peter Sanchez',
    author_email='petersanchez@gmail.com',
    license='BSD License',
    url='https://github.com/petersanchez/django-simpler-faq',
    long_description=long_description,
    platforms=['any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Environment :: Web Environment',
    ],
)
