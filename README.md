#Motor de busca

Um simples motor de busca feito como Projeto Profissional Interdisciplinar do 6º Semestre do Curso de Ciência da Computação da Faculdade Sumaré.
Isto é um programa de linha de comando escrito em Python. Os inputs que você precisará fornecer quando pedido são os seguintes:

Página Semente - Essa é a página, da qual ele começará a rastrear a web. Forneça a url de uma boa página semente, que tem amplos links nela, dessa forma você pode rastrear dentro daquelas páginas, e novamente, rastrear daquelas páginas dentro de outras páginas.

Exemplo: https://stackoverflow.com/questions/50779613/how-to-show-a-google-satelite-button-in-google-maps

Termo de busca: O termo que você quer buscar. Em breve, adicionaremos suporte para busca por multiplas palavras, mas por enquanto, use apenas uma palavra.

Exemplo: How

Profundidade máxima – O número máximo de links para se rastrear. Levarão 30 segundos para o primeiro link e 60 segundos para o segundo e continuará dobrando. Então, um máximo de 10 links é mais do que suficiente.

Exemplo:10

Depois dos 3 inputs acima, o programa começará a rodar. Poderá levar muito tempo, dependendo da profunidade especificada por você. Então o número de profundidade, será visível e irá descrescendo, sempre que um link é completamente rastreado; dessa forma quando chegar a 0, você saberá quando o rastreio terminou.
Também usamos o algoritmo "Page Rank" (presente no módulo calcula_ranks), que é exatamente o que foi utilizado nos dias iniciais do google. OS rankings da página são exibidas junto com os links após os resultados da busca serem mostrados. Então o programa os ordena, e apresenta os resultados.
Para efeitos de vizualização, nós incluímos todas estas exibições. Mas você pode comentar os trechos de “print” no módulo Procurar_novo para removê-los.
