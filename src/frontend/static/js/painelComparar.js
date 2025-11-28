document.addEventListener('DOMContentLoaded', () => {
    const planetSlides = document.querySelectorAll('.planet-slide');

    planetSlides.forEach(slide => {
        slide.addEventListener('click', (event) => {
            const painel = slide.querySelector('.painel-planet');

            painel.classList.toggle('mostrar');

            event.stopPropagation();
        });
    });


    document.addEventListener('click', (event) => {
        const todosOsPaneis = document.querySelectorAll('.painel-planet');

        todosOsPaneis.forEach(painel => {
            if (painel.classList.contains('mostrar')) {

                const cliqueDentroDoPainel = event.target.closest('.painel-planet');
                const cliqueNoGatilho = event.target.closest('.planet-slide');

                if (!cliqueDentroDoPainel && !cliqueNoGatilho) {
                    painel.classList.remove('mostrar');
                }
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const checkboxes = document.querySelectorAll('.planet-selector');
    const compareBar = document.getElementById('compare-bar');
    const countSpan = document.getElementById('count-selected');
    const btnCompare = document.getElementById('btn-compare');

    checkboxes.forEach(chk => {
        // Importante: Impede que o clique no checkbox abra o painel do planeta
        chk.addEventListener('click', (e) => {
            e.stopPropagation();
        });

        chk.addEventListener('change', atualizarBarra);
    });

    // Função para atualizar a barra flutuante
    function atualizarBarra() {
        const selecionados = document.querySelectorAll('.planet-selector:checked');
        const qtd = selecionados.length;

        // Atualiza o texto
        if (countSpan) countSpan.innerText = qtd;

        // Mostra ou esconde a barra
        if (qtd > 0) {
            compareBar.classList.add('active');
        } else {
            compareBar.classList.remove('active');
        }

        // Habilita o botão apenas com 2 ou mais
        if (btnCompare) {
            if (qtd >= 2) {
                btnCompare.disabled = false;
                btnCompare.innerText = "Comparar Planetas";
            } else {
                btnCompare.disabled = true;
                btnCompare.innerText = "Selecione mais um";
            }
        }
    }

    // Ação do Botão Comparar
    if (btnCompare) {
        btnCompare.addEventListener('click', () => {
            const selecionados = document.querySelectorAll('.planet-selector:checked');
            if (selecionados.length < 2) return;

            let nomes = [];
            selecionados.forEach(chk => nomes.push(chk.value));

            // Redireciona para a rota criada no app.py
            window.location.href = `/comparar?planetas=${encodeURIComponent(nomes.join(','))}`;
        });
    }
});