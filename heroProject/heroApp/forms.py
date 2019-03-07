from django import forms
from .models import HeroAppModel



class heroForm(forms.ModelForm):
    class Meta:
        model = HeroAppModel
        fields = '__all__'
        labels = {'question1': 'Enter Your Name',
                  'Origin': 'City/Origin',
                  'question2': 'Are You Rich or Have Super Powers',
                  'question3': 'If you have a super power, which ones?',
                  'question4': 'Which of the following are you? ',
                  'question5': 'Give us 3 examples of when you used your super hero abilities.',


        }
        widgets = {
            "question1": forms.Select(choices=[('rich', "rich"), ('superPowers', "superPowers")]),
            'question2': forms.RadioSelect(choices=[('Flight', "Flight"), ('Speed', "Speed"), ('Invisibility', "Invisibility"), ('Telekentic', "Telekentic"), ('Healing', "Healing")]),
            'question3': forms.RadioSelect(choices=[('Good', "Good"), ('kindaGood', "Kind of Good"), ('neutral', 'neutral'), ('aLittleEvil', "A Little Evil"), ('evil', "evil")]),


        }




#     Are you rich or have super powers?
# If you have a super power, which ones? (Flight, Speed, Invisibility, Telekenetic, Healing, Other)
# Which of the following are you? (Good, kinda good, neutral, a little evil, evil)
# Give us 3 examples of when you used your super hero abilities.

