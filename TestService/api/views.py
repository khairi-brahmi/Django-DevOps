from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
import pickle
import pandas
from sklearn import model_selection
from rest_framework.response import Response
from rest_framework.decorators import api_view
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes=['IsAuthenticated']

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
filename="static/ml/finalized_model.sav"
loaded_model = pickle.load(open(filename, 'rb'))

@api_view(["GET"])
def predict(request):
        result = loaded_model.score(X_test, Y_test)
        return Response({"predict ":result})
