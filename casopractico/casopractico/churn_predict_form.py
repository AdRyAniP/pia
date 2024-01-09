from flask import Flask, render_template, jsonify, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


class CustomerForm(FlaskForm):
    customer_data = StringField('Customer Data', validators=[DataRequired()])
    submit = SubmitField('Probability')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CustomerForm()
    if form.validate_on_submit():
        customer_data = form.customer_data.data
        return jsonify({'customer_data': customer_data}), 200
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
