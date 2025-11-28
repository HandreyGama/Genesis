document.addEventListener('DOMContentLoaded', function() {
    // --- Configuração dos Elementos ---
    const todosOsItens = document.querySelectorAll('.acordeao-item');
    const todosOsHeaders = document.querySelectorAll('.acordeao-header');

    // Elementos da Pesquisa
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const noResultsMessage = document.getElementById('no-results-message'); // NOVO: Mensagem de erro

    // --- Lógica do Acordeão (Abrir Apenas Um) ---
    todosOsHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const itemAtual = header.closest('.acordeao-item');

            // Fecha todos os outros itens
            todosOsItens.forEach(item => {
                if (item !== itemAtual) {
                    item.classList.remove('active');
                }
            });

            // Alterna o item clicado
            itemAtual.classList.toggle('active');
        });
    });

    // --- Lógica da Barra de Pesquisa CORRIGIDA ---

    const filtrarExoplanetas = () => {
        const termoBusca = searchInput.value.toLowerCase().trim();
        let resultadosEncontrados = 0; // Contador de resultados

        // 1. Itera sobre todos os itens e aplica o filtro
        todosOsItens.forEach(item => {
            const nomePlanetaElement = item.querySelector('.nome-planeta');

            if (nomePlanetaElement) {
                const nomePlaneta = nomePlanetaElement.textContent.toLowerCase();

                // Verifica se o item corresponde OU se o campo de busca está vazio (mostra todos)
                const corresponde = nomePlaneta.includes(termoBusca) || termoBusca === '';

                if (corresponde) {
                    item.style.display = 'list-item'; // Mostra o item
                    resultadosEncontrados++;
                } else {
                    item.style.display = 'none'; // Esconde o item
                    item.classList.remove('active'); // Garante que itens escondidos estejam fechados
                }
            }
        });

        // 2. Controla a exibição da mensagem de "nenhum resultado"
        if (resultadosEncontrados === 0 && termoBusca !== '') {
            // Se não encontrou resultados E o usuário realmente digitou algo
            noResultsMessage.style.display = 'block';
        } else {
            // Se encontrou resultados OU o campo de busca está vazio (mostrando tudo)
            noResultsMessage.style.display = 'none';
        }
    };

    // Filtra ao digitar
    searchInput.addEventListener('input', filtrarExoplanetas);

    // Filtra ao clicar no botão
    searchButton.addEventListener('click', filtrarExoplanetas);

    // Garante que o filtro seja aplicado na carga inicial para tratar o caso de lista vazia (embora improvável com Jinja)
    filtrarExoplanetas();
});