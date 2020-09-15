from setuptools import setup


setup(
      name='my_custom_sklearn_transforms',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/renatokano/sklearn_transforms/',
      author='Renato Kano',
      author_email='renatokano16@gmail.com',
      license='MIT',
      packages=[
            'my_custom_sklearn_transforms'
      ],
      zip_safe=False
)
