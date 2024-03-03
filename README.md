
# FlashCards
<p><b>Para usar, é necessário alterar a variavel pasta (no inicio do código) para uma local de pasta livre onde serão salvos os flashcards</b> </p>

<p>Revisar tudo revisa todos os flashcards que o programa julga necessário</p>
<p>Revisar matéria revisa todos os flashcards de uma matéria específica independente de se o programa julga necessário</p>
<p>Criar um card novo pergunta a qual matéria o novo card deve ser adicionado (permitindo criar uma nova) e então cria um flashcard que ficará salvo nessa matéria</p> <p>Enviar 0 no menu principal ao inves de 1, 2, 3 ou 4 retorna a lista de comandos adicionais</p>
<p> O programa julga necessário revisar o flashcard de acordo com o seguinte padrão:</p>
<ul> 
	<li> Revisa no dia seguinte em que foi criado e no próximo </li>
	<li> Depois, pula um dia e revisa mais uma vez </li>
	<li> Depois, pula 3 dias e revisa mais uma vez </li>
	<li>Depois, revisa uma vez por semana, por duas semanas </li>
	<li>Depois, revisa uma vez por mês, por 3 meses</li>
	<li>Por fim, revisa uma vez a cada aproximadamente 6 meses (185 dias)</li>
</ul>
<p>Se o usuário errar, o padrão volta do começo como se o flashcard tivesse sido criado novamente</p>
