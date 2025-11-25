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