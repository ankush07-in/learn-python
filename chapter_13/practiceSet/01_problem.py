# Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

'''
pip install virtualenv

virtualenv env1
virtualenv env2

# To activate the env1

./env1/Scripts/activate.ps1

pip install pandas
pip install pyjokes

pip freeze > requirements.txt

deactivate ( # for deactivating the env1 )

# To activate the env2
./env2/Scripts/activate.ps1

pip install -r ./requirements.txt


'''



...