from flask import Flask, request, jsonify
from datetime import datetime
from business.bonds import simple_yield_calc
from business.savings import calculate_savings
from business.inflation import calculate_inflation
from business.mortgage import calculate_monthly_mortgage
from business.ust_yield_curve import get_yield_curve_by_dates
from flask import render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('yieldCurve.html')

@app.route('/yieldCalculator')
def yieldCalculator():
    return render_template('yieldCalculator.html')

@app.route('/savingsCalculator')
def savings_calculator():
    return render_template('savingsCalculator.html')

@app.route('/inflationCalculator')
def inflation_calculator():
    return render_template('inflationCalculator.html')

@app.route('/mortgageCalculator')
def mortgage_calculator():
    return render_template('mortgageCalculator.html')

@app.route('/yieldCurve')
def yield_curve_chart():
    return render_template('yieldCurve.html')

@app.route('/calculateSavings/', methods=['POST'])
def savings_calculate():
    params = request.get_json()
    num_years = int(params['numOfYears'])
    start_amount = float(params['startAmount'])
    monthly_contrib = float(params['monthlyContribution'])
    start_year = datetime.now().year
    yld = float(params['yieldOfSavings'])
    return calculate_savings(start_amount, monthly_contrib, yld, start_year, num_years)

@app.route('/calculateBondYield/', methods=['POST'])
def calculate_bond_yield():
    content = request.get_json()
    faceValue = float(content['faceValue'])
    price = float(content['price'])
    pmtFreq = int(content['pmtFrequency'])
    coupon = float(content['coupon'])
    startDate = datetime.strptime(content['startDate'], '%Y-%m-%d')
    endDate = datetime.strptime(content['maturityDate'], '%Y-%m-%d')
    return simple_yield_calc(faceValue, price, startDate, endDate, pmtFreq, coupon, 0, pmtFreq)

@app.route('/calculateInflation/', methods=['POST'])
def calculate_inflation_for_year():
    content = request.get_json()
    curr_amount = float(content['currAmount'])
    rate = float(content['rate'])
    tartget_year = float(content['targetedYear'])
    content['calculatedAmount'] = calculate_inflation(rate, curr_amount, datetime.now().year, tartget_year)
    return content

@app.route('/calculateMortgage/', methods=['POST'])
def calculate_mortgage():
    content = request.get_json()
    principal = -1 * float(content['amountToBorrow'])
    rate = float(content['rate'])
    num_years = float(content['numYears'])
    content['monthly_payment'] = calculate_monthly_mortgage(principal, rate, num_years)
    return content

@app.route('/getYieldCurve/', methods=['POST'])
def get_yield_curve():
    content = request.get_json()
    date_strs = content['dates']
    data = get_yield_curve_by_dates([ datetime.strptime(s, '%Y-%m-%d') for s in date_strs ])
    return {"yieldData": [json.loads(data[i].to_json(orient="records"))[0] for i in range(len(data)) ]}

