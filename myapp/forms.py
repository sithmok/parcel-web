from django import forms
# from .models import Post

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title','author','money','prov','location','location2'
#                     ,'location3','location4',
#                     'position','Intern_type','body','body2',
#                     'body3','body4','body5','rating','image'
#                  )

#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'author', 'type': 'hidden'}),
#             'prov': forms.Select(attrs={'class': 'form-control', 'value':'', 'id': 'prov'}),
#             'location': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': "ซอย" }),
#             'location2': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': "ถนน"}),
#             'location3': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': "ตำบล"}),
#             'location4': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': "อำเภอ"}),
#             'position': forms.TextInput(attrs={'class': 'form-control'}),
#             'Intern_type': forms.Select(attrs={'class': 'form-control'}),
#             'money': forms.TextInput(attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control'}),
#             'body2': forms.Textarea(attrs={'class': 'form-control'}),
#             'body3': forms.Textarea(attrs={'class': 'form-control'}),
#             'body4': forms.Textarea(attrs={'class': 'form-control'}),
#             'body5': forms.Textarea(attrs={'class': 'form-control'}),
#             'rating': forms.Select(attrs={'class': 'form-control'}),
#             'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
#         }