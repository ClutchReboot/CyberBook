from setuptools import setup

# python setup.py sdist
# twine upload dist/*

setup(name='TechBook',
      version='0.0.6',
      description='Spellbook for coders.',
      url='https://github.com/ClutchTech/TechBook',
      keywords='techbook encoders tools',
      author='Clutch_Reboot',
      author_email='clutchshadow26@gmail.com',
      license='GNU General Public License v3.0',
      packages=['TechBook.CrypticItems', 'TechBook.FileSystemMagic', 'TechBook.NetworkConjuration'],
      zip_safe=False,
      long_description=open('README.md', 'rt').read(),
      long_description_content_type='text/markdown',
      python_requires='>=3.10',
      )
