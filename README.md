#Motor de busca

Isto é um programa de linha de comando escrito em Python. A grande maioria dos Sistemas Operacionais baseados em Unix já vem com o interpretador Python na versão 2.X instalado por padrão. Para Windows, basta fazer o download em: https://www.python.org/download/releases/2.7.2/

Os inputs que você precisará fornecer quando solicitado, são os seguintes:

Página Semente - Essa é a página, da qual ele começará a rastrear a web. Forneça a URL de uma boa página semente, que tem muitos links nela, dessa forma você pode rastrear dentro daquelas páginas, e novamente, rastrear daquelas páginas dentro de outras páginas.

Exemplo: https://webdevacademy.com.br/tutoriais/bootstrap-como-comecar/

Termo de busca: O termo que você quer buscar. Em breve, adicionaremos suporte para busca por multiplas palavras, mas por enquanto, use apenas uma palavra.

Exemplo: Bootstrap

Profundidade máxima – O número máximo de links para se rastrear. Levarão 3 segundos para o primeiro link e 6 segundos para o segundo e continuará dobrando. Então, um máximo de 10 links é mais do que suficiente.

Exemplo:10

Depois dos 3 inputs acima, o programa começará a rodar. Poderá levar muito tempo, dependendo da profunidade especificada por você. Então o número de profundidade, será visível e irá descrescendo, sempre que um link é completamente rastreado; dessa forma quando chegar a 0, você saberá quando o rastreio terminou.
Também usamos o algoritmo "Page Rank" (presente no módulo calcula_ranks), que é exatamente o que foi utilizado nos dias iniciais do google. OS rankings da página são exibidos junto com os links após os resultados da busca serem mostrados. Então o programa os ordena, e apresenta os resultados.
Para efeitos de vizualização, nós incluímos todas estas exibições. Mas você pode comentar os trechos de “print” no módulo Procurar_novo para removê-los.
