from django import forms

# from phonenumber_field.formfields import PhoneNumberField

spice_choices=(
        ("choose your spice level","choose your spice level"),
        ( "low","low"),
        ("medium","medium"),
        ("high","high"),
    )
# class PostOrder1(forms.ModelForm):
#
#     class Meta:
#         model=Order
#         fields=['First_Name','Last_Name','Email','Phone_Number','Your_Order','Spice_Choice']

class PostOrder(forms.Form):
    FirstName=forms.CharField(max_length=20,label='',
            widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))
    LastName = forms.CharField(max_length=20, label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))
    Email=forms.EmailField(label='',
                           widget=forms.TextInput(attrs={'placeholder':'Email Id'}))
    # PhoneNumber=PhoneNumberField(label='',
    #                             widget= forms.TextInput(attrs={'placeholder':'Phone number'}))
    PhoneNumber = forms.CharField(label=' ',widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    OrderDetails = forms.CharField(label=' ', widget= forms.Textarea(attrs={'rows':3,'columns':20,
                                                'placeholder':'Enter your order details please'}))



    Spice_Choice=forms.ChoiceField(choices=spice_choices,label='')