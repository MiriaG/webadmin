#git push -u origin master comando para salvar no github 


from flask import Flask , render_template

app=Flask(__name__)


@app.route ("/") #MAPEANDO AS FUNÇÕES 
def index ():
	return "CHEGA DE ICS"

@app.route ("/pagina") #MAPEANDO AS FUNÇÕES 
def pagina ():
	return render_template ("index.html")

@app.route ("/nmap") #MAPEANDO AS FUNÇÕES 
def nmap ():
	import subprocess
	proc = subprocess.Popen (['nmap', '-sP','10.120.71.*'],stdout=subprocess.PIPE)
	ret=proc.stdout.read()
	return ret

@app.route ("/test") #MAPEANDO AS FUNÇÕES 
def teste ():
	return "<input type='submit' value='intervalo'></imput>"

app.run (debug=True, host="0.0.0") #MODO DE DEPURAÇÃO, ATUALIZA SOZINHO
