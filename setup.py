import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dictpp-utksara", # Replace with your own username
    version="0.0.1",
    author="Utkarsh Saraswat",
    author_email="saraswat.utk@gmail.com",
    description="Package used to merege two dictionaries without attenuating or overwriting any values",
    long_description="Let's say there are two dictionaries in python dic1 and dic2, then the merge results for different cases are enlisted below-" + \
                     "case 1: dic1 = {a : {c : {d: end}}} and dic2 = {a : {e : {f : end}}}" + \
                            "merged dictionary = {a : {c : {d: end}, e : {f : end}}} " + \
                     "case 2: dic1 = {a : {b : end}} and dic2 = {a : b }" + \
                            "merged dictionary = {a : {b : end}}"+ \
                     "case 3: dic1 = {a : {c : end}} and dic2 = {a : {c : END}}" + \
                            "merged dictionary = {a : b : {c : [end, END]}}"+ \
                     "case 4: dic1 = {x : {z : end}} and dic2 = {a : {c : end}}" + \
                            "merged dictionary = {x : {z : end},a : {c : end}}"+ \
                     "case 5: dic1 = {x : {z : end}, l : {n : end}} and dic2 = {a : {c : end}, l : {n : end}}" + \
                            "merged dictionary = {x : {z : end}, l : {n : end}}, a : {c : end}}"+ \,
                     "case 5: dic1 = {x : {z : end}, l : {n : end}} and dic2 = {a : {c : end}, l : {n : end}}" + \
                            "merged dictionary = {x : {z : end}, l : {n : end}}, a : {c : end}}"+ \,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)