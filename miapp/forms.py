from django import forms
class formdocente(forms.Form):

    codigo = forms.CharField(label="Codigo: ")
    nombre = forms.CharField(label="Nombre: ")
    Apellido_Paterno = forms.CharField(label="Apellido Paterno: ")
    Apellido_Materno = forms.CharField(label="Apellido Materno: ")
    DNI = forms.CharField(label="DNI: ")
    Fecha_Nacimiento = forms.DateField(label="Fecha de nacimiento: ")
    Estado = forms.CharField(label="Estado: ")