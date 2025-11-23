document.addEventListener('DOMContentLoaded', () => {
    const botao_download_gatilho = document.querySelector(".botao_download");
    const aviso_box = document.querySelector("#aviso-download-box");
    const botao_sim = document.querySelector(".botao-sim");
    const botao_nao = document.querySelector(".botao-nao");

    let autoCloseTimeout;

    function hideAviso() {
        aviso_box.style.display = 'none';
        clearTimeout(autoCloseTimeout);
    }

    botao_download_gatilho.addEventListener('click', () => {

        if (aviso_box.style.display === 'block' || aviso_box.style.display === 'inline') {
            hideAviso();
            return;
        }

        aviso_box.style.display = 'block'; // Mostra o aviso

        autoCloseTimeout = setTimeout(() => {
            hideAviso();
        }, 5000);
    });

    // Evento de clique no botão "Sim"
    botao_sim.addEventListener('click', () => {
        const downloadUrl = botao_sim.getAttribute('data-download-url');
        window.location.href = downloadUrl;


        hideAviso();
    });


    botao_nao.addEventListener('click', () => {
        hideAviso();
    });
});