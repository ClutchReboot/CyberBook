from setuptools import setup

# python setup.py sdist
# twine upload dist/*

setup(name='CyberBook',
      version='0.0.24',
      description='Cyber spellbook for developers.',
      keywords='cyberbook DecoderRing tools',
      author='Clutch_Reboot',
      author_email='clutchshadow26@gmail.com',
      license='GNU General Public License v3.0',
      packages=[
            'CyberBook',
            'CyberBook.ConjureTraversalList',
            'CyberBook.DecoderRing',
            'CyberBook.SummoningCircle',
            'CyberBook.Identify',
            'CyberBook.Misc'
      ],
      zip_safe=False,
      long_description=open('README.md', 'rt').read(),
      long_description_content_type='text/markdown',
      python_requires='>=3.10',
      install_requires=[
            'requests',
            'urllib3',
            'netifaces'
      ],
      project_urls={
            "Documentation": "https://clutchreboot.github.io/CyberBookDocs/",
            "Source": "https://github.com/ClutchReboot/CyberBook",
      },
      )
