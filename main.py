from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/",methods=["GET","POST"])


def calcultor_main():
    if request.method=="POST":
        resp = request.form
        stud_nm = resp.get('nm')
        a = resp.get('fnum')
        b = resp.get('snum')
        c = resp.get('tnum')
        d = resp.get('frnum')
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        result = ((a+b+c+d)/4)


        return render_template("result.html",resp=result,num1=a,num2=b,num3=c,num4=d,num0=stud_nm)
    else:

        return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)