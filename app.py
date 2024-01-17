import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, request, url_for

model = pickle.load(open("model.pkl", "rb"))
df = pickle.load(open("dataframe.pkl", "rb"))

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    company_name = request.form["companyname"]
    type_name = request.form["typename"]
    ram = float(request.form["ram"])
    weight = float(request.form["weight"])
    cpu_brand = request.form["cpuBrand"]
    gpu_brand = request.form["gpuBrand"]
    op_sys = request.form["opsys"]
    screen_size = float(request.form["inch"])
    x_res = int(request.form["xResolution"])
    y_res = int(request.form["yResolution"])
    hdd_size = int(request.form["hddSize"])
    ssd_size = int(request.form["ssdsize"])
    touch_screen = 1 if request.form["touchscreen"] == "Yes" else 0
    ips = 1 if request.form["ips"] == "Yes" else 0
    hd = 1 if request.form["hd"] == "Yes" else 0

    PPI = np.sqrt(x_res**2 + y_res**2) / screen_size

    inp_list = np.array([
        company_name,
        type_name,
        ram,
        op_sys,
        weight,
        touch_screen,
        ips,
        hd,
        PPI,
        cpu_brand,
        hdd_size,
        ssd_size,
        gpu_brand,
    ]).reshape(1, -1)

    df_inp = pd.DataFrame(inp_list, columns=df.drop("Price", axis=1).columns)

    prediction = model.predict(df_inp)
    prediction = round(prediction[0], 2)

    price = np.exp(prediction)

    return render_template("index.html", prediction=price)


if __name__ == "__main__":
    app.run(debug=True)
