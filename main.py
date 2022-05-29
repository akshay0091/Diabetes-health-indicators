from flask import Flask, render_template,request, url_for, redirect
import pickle

app = Flask(__name__)
model=pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        HighBP = request.form['HighBP']
        HighChol = request.form['HighChol']
        CholCheck = request.form['CholCheck']
        BMI = request.form['BMI']
        Smoker = request.form['Smoker']
        Stroke = request.form['Stroke']
        HeartDiseaseorAttack = request.form['HeartDiseaseorAttack']
        PhysActivity = request.form['PhysActivity']
        Fruits = request.form['Fruits']
        Veggies = request.form['Veggies']
        HvyAlcoholConsump = request.form['HvyAlcoholConsump']
        Sex = request.form['Sex']
        Age = request.form['Age']
       # Username=request.form['Username']
        prediction = model.predict([[
            HighBP,
            HighChol,
            CholCheck,
            BMI,
            Smoker,
            Stroke,
            HeartDiseaseorAttack,
            PhysActivity,Fruits,
            Veggies,
            HvyAlcoholConsump,
            Sex,
            Age,


        ]])
        number = int(prediction)
        print(prediction)
        if (number==0):
            output='No chance Diabetes'
        elif (number==1):
            output='prediabetes stage '
        else:
            output='diabetes'
            return output


        return redirect(url_for('result',output=output))
    return render_template('home.html')

@app.route('/result')
def result():

    output=request.args.get('output',None)
    return render_template('result.html',output=output)
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run()