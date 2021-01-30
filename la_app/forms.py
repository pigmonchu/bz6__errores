from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField, ValidationError, HiddenField
from wtforms.validators import DataRequired
from datetime import date

class DifferentFrom:
    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name {}.".format(self.fieldname)))
        
        if field.data == other.data:
            d = {
                'other_label': hasattr(other, 'label') and other.label.text or self.fieldname, 'other_name': self.fieldname
            }
            if self.message is None:
                self.message = field.gettext('Field must be different to {}')
            raise ValidationError(self.message.format(other.data))

class TransactionForm(FlaskForm):
    currencys_from = SelectField(validators=[DataRequired()])
    currencys_to = SelectField(choices=["EUR", "BTC","ETH","BNB","LTC"], validators=[DataRequired(), DifferentFrom("currencys_from")])
    quantity_from = FloatField(validators=[DataRequired()])
    quantity_to = HiddenField()

    calc = SubmitField("")
    accept = SubmitField("")

