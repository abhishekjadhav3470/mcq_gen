from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='abhishekjadhav',
    author_email='abhishek.jadhav2@pw.live',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)