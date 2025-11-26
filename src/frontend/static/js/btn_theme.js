// Define as variáveis de cor e imagem para os temas
const themes = {
    light: {
        '--color_text--': 'black',
        '--color_bg--': 'white',
        '--color-btn-theme--': 'white',
        // Ícone da Lua para o tema claro (sugere que o usuário pode mudar para escuro)
        '--btn-image-url--': 'url("/static/img/Moon.png")' 
    },
    dark: {
        '--color_text--': 'white',
        '--color_bg--': '#1e1e1e', // Um fundo escuro (exemplo)
        '--color-btn-theme--': '#333',
        // Ícone do Sol para o tema escuro (sugere que o usuário pode mudar para claro)
        '--btn-image-url--': 'url("/static/img/Sun.png")' 
    }
};

const rootElement = document.documentElement; // Referência ao :root (elemento <html>)

/**
 * Obtém o valor atual de uma variável CSS do :root (Leitura).
 */
function getCssVariable(variableName) {
    // Usamos getComputedStyle para ler o valor que está sendo aplicado
    const computedStyle = getComputedStyle(rootElement);
    return computedStyle.getPropertyValue(variableName).trim();
}

/**
 * Define o valor de uma variável CSS no :root (Escrita).
 */
function setCssVariable(variableName, value) {
    rootElement.style.setProperty(variableName, value);
}

/**
 * Alterna entre o tema claro e o tema escuro.
 */
function toggleTheme() {
    // Verifica o valor atual de --color_bg-- para determinar o tema atual
    const currentBg = getCssVariable('--color_bg--');
    let newTheme;
    let newThemeName;
    
    // O valor de 'white' pode ter espaços, então verificamos se é o tema claro.
    if (currentBg.includes(themes.light['--color_bg--'])) {
        // Se for claro, muda para escuro
        newTheme = themes.dark;
        newThemeName = 'dark';
    } else {
        // Se for escuro (ou qualquer outro valor, volta para o claro)
        newTheme = themes.light;
        newThemeName = 'light';
    } 

    // Aplica as novas cores e imagem de fundo do botão (Lua ou Sol)
    for (const [variable, value] of Object.entries(newTheme)) {
        setCssVariable(variable, value);
    }
    
    // Salva a preferência no armazenamento local para que persista
    localStorage.setItem('theme', newThemeName);
}

/**
 * Aplica o tema salvo (ou o padrão) ao carregar a página.
 */
function applySavedTheme() {
    const savedTheme = localStorage.getItem('theme');
    let initialTheme = themes.light; // Padrão é tema claro

    if (savedTheme === 'dark') {
         initialTheme = themes.dark;
    }
    
    // Aplica as variáveis iniciais
    for (const [variable, value] of Object.entries(initialTheme)) {
        setCssVariable(variable, value);
    }
}

// 2. Adiciona o Listener de Evento ao Botão quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
    // 1. Aplica o tema salvo imediatamente
    applySavedTheme(); 
    
    const themeButton = document.querySelector('.btn_theme');

    if (themeButton) {
        // 2. Adiciona o listener para a função de alternância completa
        themeButton.addEventListener('click', toggleTheme);
    }
});