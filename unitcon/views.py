"""views en django se utiliza para conectar los paginas html y tambien para escribir logicas
y funciones de la pagina"""

from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})


"""El logic del unit converter, lo se que se puede crear con el 
control flow del python(conditional-if, functions, input, loops, operators)pero, en el momento, no me sale
la combinacion de syntax ya que tenemos que hacer la prueba si ver a ningun tutorial"""
