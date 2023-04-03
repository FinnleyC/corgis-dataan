from flask import Flask, url_for, render_template, request, Markup
import json
import multidict

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('res.html')

@app.route("/s")
def render_stats():
    with open("cars.json") as cars:
        car_data = json.load(cars)
    if 'lor' in request.args and 'upr' in request.args:
        lor = int(request.args['lor'])
        upr = int(request.args['upr'])
        c = multidict.MultiDict()
        for data in car_data:
            if data['Engine Information']['Engine Statistics']['Horsepower'] >= lor and data['Engine Information']['Engine Statistics']['Horsepower'] <= upr:
                c.add(str(data['Engine Information']['Engine Statistics']['Horsepower']), data['Identification']['ID'])
        c = sorted(c.items())
        result = ''
        for key in c:
            result += Markup("<tr><td>" + key[0] + "</td><td>" + key[1] + "</td>" + "</tr>")
        return render_template('statshow.html', table = result)
    return render_template('stat.html')

@app.route("/nul")
def render_page2():
    return render_template('2.html')




def researchproject():
    with open("cars.json") as cars:
        car_data = json.load(cars)

    makes = [] #begins empty list
    makesn = 0 #creates empty variable
    for data in car_data:
        if data['Identification']['Make'] not in makes: #if the make is not one already found:
            makes.append(data['Identification']['Make']) #adds make name to list of makes
            makesn = makesn + 1 #add one to makesn (number of makes)
    print(makes) #prints list of makes
    print(makesn) #prints number of unique makes

    hp = 0
    tq = 0
    name = ''
    for data in car_data:
        if data['Engine Information']['Engine Statistics']['Horsepower'] > hp and data['Engine Information']['Engine Statistics']['Torque'] > tq:
            hp = data['Engine Information']['Engine Statistics']['Horsepower']
            tq = data['Engine Information']['Engine Statistics']['Torque']
            name = data['Identification']['ID']
    print(hp)
    print(tq)
    print(name)
    
if __name__=="__main__":
    app.run(debug=True)
