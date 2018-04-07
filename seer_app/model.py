from wtforms import Form, SelectField, validators
from compute import generate_tuples

class SimpleForm(Form):
  
    tuples = generate_tuples()

    X_axis = SelectField('Categorical Variables',
                    choices=tuples[0],
                    validators=[validators.InputRequired()])
    Y_axis = SelectField('Continuous Variables',
                    choices=tuples[1],
                    validators=[validators.InputRequired()])

