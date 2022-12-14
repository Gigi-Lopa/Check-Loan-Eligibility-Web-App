from typing import Type
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from loan_app.models import userDetails, userLoanDetails, adminUser
from django.http import HttpResponseRedirect
import json
# Create your views here

def home(request):
    return render(request, "login.html")
def mainPage(request):
    if request.session.get("username"):
        details = userLoanDetails.objects.filter(userId = request.session.get("userId"))
        return render(request,"index.html",{
        "username": request.session.get("username"),
        "userId": request.session.get("userId"),
        "userloandetails": details
        } )
    else:
        return HttpResponseRedirect("/")
@csrf_exempt
def logIn(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
        logDetails = userDetails.objects.get(username = username, password  = password) 
        if logDetails:
            request.session["userId"]  = logDetails.id
            request.session["username"]= logDetails.username
            return HttpResponseRedirect("/home/") 
    except:
        return HttpResponseRedirect("/")
def renderCreateAccount(request):
    return render(request, "sign-up.html")
@csrf_exempt
def addUsers(request):
    name = request.POST["username"]
    email = request.POST["email"]
    password  =request.POST["password"]
    userObj = userDetails(username = name, email =email, password = password )
    userObj.save()
    #Add users here
    return HttpResponseRedirect("/")
def addUserHistory(userStories):
    logDetails = userDetails.objects.get(id = userStories[11])
    if logDetails:
        logDetails.userloandetails_set.create(
        gender = userStories[0],
        married = userStories[1],
        dependents = userStories[2],
        education = userStories[3],
        employment = userStories[4],
        income = userStories[5],
        coappIncome = userStories[6],
        loanAmount = userStories[7],
        loanAmountTerm = userStories[8],
        creditHistory = 1.0,
        area = userStories[9],
        assets = userStories[10],
        loanStatus = userStories[12]
        )    
        return True
def logisticRegression(x, y, test):
    from sklearn.model_selection import train_test_split
    x_train, x_cv, y_train, y_cv = train_test_split(x, y, train_size=0.75, random_state=0)
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    model.fit(x_train, y_train)
    pred_cv = model.predict(x_cv)
    print("============FIRST MODEL PREDICTED =========")
    from sklearn.metrics import confusion_matrix
    c = confusion_matrix(y_cv, pred_cv)
    pred_test = model.predict(test.tail(1))
    return pred_test

def randomForest(x, y, test):
    from sklearn.tree import DecisionTreeClassifier
    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier.fit(x, y)
    pred_test = classifier.predict(test.tail(1))
    return pred_test

def decisionTrees(x, y, test):
    from sklearn import tree
    from sklearn.model_selection import StratifiedKFold
    i = 1
    kf = StratifiedKFold(n_splits=5, random_state=1, shuffle=True)
    for train_index, test_index in kf.split(x, y):
        xtr, xvl = x.loc[train_index], x.loc[test_index]
        ytr, yvl = y[train_index], y[test_index]
        model = tree.DecisionTreeClassifier(random_state=1)
        model.fit(xtr, ytr)
        pred_test_xvl = model.predict(xvl)
        i += 1
    pred_test = model.predict(test.tail(1))
    return pred_test
@csrf_exempt
def predictions(request):
        print("==== INTIALIZING PROTOCOLS =====")
        import pandas as pd                       # for reading the files
        import numpy as np                        # for creating multi-dimensional-array
        test = pd.read_csv("test.csv")
        train = pd.read_csv("train.csv")
        # TEST HANDLING
        test['Gender'].fillna(test['Gender'].mode()[0], inplace=True)
        test['Married'].fillna(test['Married'].mode()[0], inplace=True)
        test['Self_Employed'].fillna(test['Self_Employed'].mode()[0], inplace=True)
        test['Loan_Amount_Term'].fillna(test['Loan_Amount_Term'].mode()[0], inplace=True)
        test['LoanAmount'].fillna(test['LoanAmount'].median(), inplace=True)
        test['Assets'] = np.random.randint(5700, 9000, test.shape[0])
        test.Dependents = test.Dependents.fillna('0')
        test.Credit_History = test.Credit_History.fillna(1.0)
        print("===== TEST DATA CLEANED =====")
        #======= GET INPUT FROM USER ========#
        cols = ["Loan_ID", "Gender", "Married", "Dependents", "Education", "Self_Employed", "ApplicantIncome",
                "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History", "Property_Area", "Assets"]
        if request.method == "POST":
            userStories = []
            Gender = request.POST.get("Gender")
            userStories.append(Gender)
            Married = request.POST["Married"]
            userStories.append(Married)
            Dependents = request.POST["Dependents"]
            userStories.append(Dependents)
            Education = request.POST["Graduate"]
            userStories.append(Education)
            Self_Employed = request.POST["Employment"]
            userStories.append(Self_Employed)
            ApplicantIncome = int(request.POST["ApplicantIncome"])
            userStories.append(ApplicantIncome)
            CoapplicantIncome = int(request.POST["CoapplicantAmount"])
            userStories.append(CoapplicantIncome)
            LoanAmount = float(request.POST["LoanAmount"])
            userStories.append(LoanAmount)
            request.session["loanAmount"] = LoanAmount
            Loan_Amount_Term = float(request.POST["Payment_terms"])
            userStories.append(Loan_Amount_Term)
            Credit_History = float(1.0)
            Property_Area = request.POST["property_area"]
            userStories.append(Property_Area)
            Assets = np.int32(request.POST["assets"])
            userStories.append(Assets)
            userId = int(request.POST["user_id"])
            userStories.append(userId)
            model = request.POST["regression_model"]
            loan_id = "LP002989"
            user_infor = [loan_id, Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
                        CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area,
                        Assets]
            new_df = pd.DataFrame([user_infor], columns=cols)
            print("===== NEW DATAFRAME MADE ==========")
            test = pd.concat([test, new_df], ignore_index=True)
            test = test.drop("Loan_ID", axis=1)
            train = train.drop("Loan_ID", axis=1)
            x = train.drop('Loan_Status', axis=1)
            y = train['Loan_Status']
            x = pd.get_dummies(x)
            test = pd.get_dummies(test)
            print("======= DUMMY VARIABLES GENERATED =========")
            if model == "Logistic Regression":
                pred_test = logisticRegression(x, y, test)
                userStories.append(pred_test)
                if addUserHistory(userStories):
                    return render(request, "results.html", {"data": pred_test[0], 
                    "LoanAmount": request.session.get("loanAmount")})
            
            elif model == "Random Forest":
                pred_test = randomForest(x,y,test)
                userStories.append(pred_test)
                if addUserHistory(userStories):
                    return render(request, "results.html", {"data": pred_test[0], 
                    "LoanAmount": request.session.get("loanAmount")})

            elif model == "Decision Tree":
                pred_test = decisionTrees(x, y, test)
                userStories.append(pred_test)
                if addUserHistory(userStories):
                    return render(request, "results.html", {"data": pred_test[0],
                     "LoanAmount": request.session.get("loanAmount")})
def adminPage(request):
    return render(request , "adminAcc.html")
@csrf_exempt
def authAdmin(request):
    adminUserName = request.POST["adminusername"]
    adminPassword = request.POST["adminpassword"]
    adminObj = adminUser.objects.get(adminusername = adminUserName, adminpassword = adminPassword)
    if adminObj:
        request.session["adminAuth"] = True
        return HttpResponseRedirect("/home/admin")
def homeAdmin(request):
    if request.session.get("adminAuth"):
        userDetailsList = userDetails.objects.all()
        userLoanDetailsList = userLoanDetails.objects.all()
        return render(request, "homeAdmin.html", {
            "userDetailsList":userDetailsList,
            "userLoanDetailsList":userLoanDetailsList
            })
    else:
        return HttpResponseRedirect("/admin/admin123/")