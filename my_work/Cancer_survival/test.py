import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load('dumped_model.pkl')
data = model.predict([[55, 45,8]])
print(data[0])

if data[0] ==1:
    print('The patient will survive 5 years or longer')
else:
    print('The patient will die within 5 year')


print('\n\n------------------Well Done----------------------------')