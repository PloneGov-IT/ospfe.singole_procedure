from setuptools import setup, find_packages
import os

version = '0.2.1.dev0'

setup(name='ospfe.singole_procedure',
      version=version,
      description="Pubblicazione dei dati ai sensi dell'art. 1 comma 32 Legge n. 190/2012, con collective.tablepage",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Programming Language :: Python",
        ],
      keywords='plone plonegov trasparenza singole-procedure',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://github.com/PloneGov-IT/ospfe.singole_procedure',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ospfe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'lxml',
          'collective.tablepage>=0.5b2'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
